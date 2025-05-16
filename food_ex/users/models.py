from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    