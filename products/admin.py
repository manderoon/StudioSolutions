from django.contrib import admin
from . import models

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Product, ProductsAdmin)

