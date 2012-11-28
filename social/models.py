from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Circle(models.Model):
    '''A circle of users, similar to Google+ circles'''
    
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, related_name="user")
    members = models.ManyToManyField(User, related_name="members")
    
    def __unicode__(self):
        return self.name