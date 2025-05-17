from django.db import models


class Price(models.Model):
    product = models.ForeignKey('product_repository.Product', on_delete=models.CASCADE)
    base_price = models.FloatField()
    
    def __str__(self):
        return f"{self.product}: {self.base_price}"
    
    
class PriceCalculation(models.Model):
    calculated_price = models.FloatField()
    order_id = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order: {self.order_id} calculated price: {self.calculated_price}"