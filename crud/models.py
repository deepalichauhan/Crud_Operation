from turtle import title
from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    address = models.CharField(max_length=100)

def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.address




