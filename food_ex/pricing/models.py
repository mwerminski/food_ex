from django.db import models


class Price(models.Model):
    product = models.ForeignKey('product_repository.Product', on_delete=models.CASCADE)
    base_price = models.FloatField()
    
    def __str__(self):
        return self.base_price
    
class CalculatedPrice(models.Model):
    calculated_order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('product_repository.Product', on_delete=models.CASCADE)
    calculated_price = models.FloatField()
        
    def __str__(self):
        return self.calculated_price