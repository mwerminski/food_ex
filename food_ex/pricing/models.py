from django.db import models


class Price(models.Model):
    product = models.ForeignKey('product_repository.Product', on_delete=models.CASCADE)
    base_price = models.FloatField()
    
    def __str__(self):
        return f"{self.product}: {self.base_price}"