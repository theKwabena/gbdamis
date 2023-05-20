from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    event = models.CharField(max_length=255)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)