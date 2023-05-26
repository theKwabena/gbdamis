from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)

from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, blank=True)
    first_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank =True, null=True)
    whatsapp_number = models.CharField(max_length=255, default = 'Same as Phone Number', blank=True, null=True)
    company_name = models.CharField(max_length=255,blank=True, null=True)
    region_or_zone = models.ForeignKey('Zone', on_delete=models.SET_NULL, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    field = models.ForeignKey('Field', on_delete=models.SET_NULL, null=True, blank=True)
    drilling_licence = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255,null=True, blank=True)
    referee = models.CharField(max_length=255,null=True, blank=True)
    referee_contact = models.CharField(max_length=255, null=True, blank=True)


    active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    profile_complete = models.BooleanField(default=False)
 
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'username'
    #Email and Password are required by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.other_names}"
    
    def get_short_name(self):
        return f"{self.first_name} {self.other_names}"
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def profile_completed(self):
        return self.profile_complete
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_verified(self):
        return self.verified
    

    def generate_username(self):
        # Generate the username based on first name and last name
        other_names = self.other_names.split(' ')
        generated = ' '
        if len(other_names) ==2:
            generated = self.first_name[0].lower() + other_names[0][0].lower() + other_names[1].lower()
        elif len(other_names)==3:
            generated = self.first_name[0].lower() + other_names[0][0].lower() + other_names[-1].lower()
        else:
            generated = self.first_name[0].lower() + other_names[-1].lower()

        # Check if the generated username already exists
        existing_users = User.objects.filter(username=generated)
        if existing_users.exists():
        # Append a number to the username if it already exists
            num = 1
            while existing_users.exists():
                generated = f"{generated}{num}"
                num += 1
                existing_users = User.objects.filter(username=generated)
        username = generated
        return username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.generate_username()
        if self.whatsapp_number == 'Same as Phone Number':
            self.whatsapp_number = self.phone_number  # Set field2 to the value of field1 if field2 is empty
        super().save(*args, **kwargs)
    


class Zone(models.Model):
    name = models.CharField(max_length=255)
    zone_suffix = models.CharField(max_length=5)


class Field(models.Model):
    name = models.CharField(max_length=255)