from django import forms
from django.conf import settings
from django.db import models



# Create your models here.
class Nomination(models.Model):
    nominee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nominee.get_full_name()}: {self.position}"
    
    
    
class Position(models.Model):
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null =True, blank=True)
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    def __str__(self):
        return self.name