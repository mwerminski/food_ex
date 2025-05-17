from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.username)
    
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.full_name)
    