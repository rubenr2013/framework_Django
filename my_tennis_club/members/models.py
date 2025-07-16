from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(max_length=255, null=True)
    