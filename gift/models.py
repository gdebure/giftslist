from django.db import models
from django.auth import User

# Create your models here.

class List(models.Model):
    
    name = models.CharField(max_length=128)
    target_date = models.DateField()
    owner = models.ForeignKey(User)
    

class Gift(models.Model):
    
    STATUS_CHOICES = (
                       ('W','Wished'), # Not Offered Yet
                       ('R','Reserved'), # Someone committed to offer it, making it unavailable for others
                       ('O','Offered'), # This gift has been offered,  making it unavailable for others
                    )
                    
    name = models.CharField(max_length=256)
    description = models.TextField()
    list = models.ManyToManyField(List)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    
    
class GiftLink(models.Model):
    
    gift = models.ForeignKey(Gift)
    url = models.UrlField()
    
