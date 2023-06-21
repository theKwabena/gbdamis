from datetime import datetime
from django.db import models
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from django.contrib.auth.models import (
    AbstractBaseUser
)

from gbdamis.dues.models import Dues


from .tasks import send_email
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
    drilling_license = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255,null=True, blank=True)
    referee = models.CharField(max_length=255,null=True, blank=True)
    referee_contact = models.CharField(max_length=255, null=True, blank=True)

    approved = models.BooleanField(default =False)
    active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    # profile_complete = models.BooleanField(default=False)
 
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'username'
    #Email and Password are required by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.other_names}"
    
    @property
    def get_short_name(self):
        return f"{self.first_name} {self.other_names}"
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    
    @property
    def profile_completed(self):
        if self.region_or_zone or self.whatsapp_number or self.field:
            return True
        else:
            return False
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_verified(self):
        return self.verified
    
    @property
    def get_accumulated_dues(self):
        dues = Dues.objects.filter(user=self, paid=False)
        amount = 0
        for due in dues:
            amount += due.amount
        if amount == 0:
            return None
        else:
            return amount
    
    # get the current due owned by the user by the current month and year
    @property
    def get_current_due(self):
        monthly_dues = Dues.objects.get(user=self, paid=False, month__month=datetime.now().month, month__year=datetime.now().year)
        return monthly_dues
        
    
    # get all dues owned by the user
    @property
    def get_all_dues(self):
        dues = Dues.objects.filter(user=self)
        return dues
    
    
    def approve_user(self):
        self.approved = True
        self.save()
        email_subject = 'Welcome to GBDAMIS'
        email_body = render_to_string('emails/welcome_email.html', {
            'user': self,
        })
        send_email.delay(subject = email_subject, body = email_body,  recipient = self.email)
      
        return self.approved
    
    def decline_user(self):
        self.declined = True
        self.save()
        return self.declined
    
    def verify_user(self):
        self.verified = True
        self.save()
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

        # send admin message on save
        super().save(*args, **kwargs)


    # get the amount owned by the user using the dues model, select all dues where the user is the user and paid is false
    
    


class Zone(models.Model):
    name = models.CharField(max_length=255)
    zone_suffix = models.CharField(max_length=5)


class Field(models.Model):
    name = models.CharField(max_length=255)