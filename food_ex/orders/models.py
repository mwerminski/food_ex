from django.db import models


class OrderStatus(models.TextChoices):
    CREATED = 'CREATED'
    PREPARED = 'PREPARED'
    DELIVERING = 'DELIVERING'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'
    RETURNED = 'RETURNED'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    products = models.ManyToManyField('product_repository.Product')
    calculated_price = models.ManyToManyField('pricing.CalculatedPrice')
    final_price = models.FloatField()
    
    retailer = models.ForeignKey('users.Company', on_delete=models.CASCADE)
    client = models.ForeignKey('users.User', on_delete=models.CASCADE)
    distance = models.FloatField()
    location = models.CharField(max_length=200)
    
    created_at = models.DateTimeField()
    finished_at = models.DateTimeField() 
    
    status = models.CharField(
        max_length=15,
        choices=OrderStatus.choices,
        default=OrderStatus.CREATED,
    )
    
    def __str__(self):
        return f"{self.retailer}_{self.client}_{self.order_id}"
    