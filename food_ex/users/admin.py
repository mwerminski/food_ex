from django.contrib import admin

from .models import Client
from .models import Company

admin.site.register(Client)
admin.site.register(Company)