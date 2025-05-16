from django.db import models


class ProductType(models.TextChoices):
    DRINK = 'DRINK'
    FOOD = 'FOOD'
    SET = 'SET'
    UNKNOWN = 'UNKNOWN'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    product_type = models.CharField(
        max_length=15,
        choices=ProductType.choices,
        default=ProductType.UNKNOWN,
    )
    
    def __str__(self):
        return self.name
