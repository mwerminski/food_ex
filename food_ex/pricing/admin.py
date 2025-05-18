from django.contrib import admin
from .models import Price
from .models import PriceCalculation

admin.site.register(Price)
admin.site.register(PriceCalculation)