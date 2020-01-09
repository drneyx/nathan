from __future__ import unicode_literals
from django.db import models


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    emailaddress = models.CharField(max_length=30)
    emp_id = models.CharField(max_length=10)
    password = models.CharField(max_length=14)
    confirmpassword = models.CharField(max_length=14)
    
