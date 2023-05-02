from django.contrib import admin
from . import models

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_id')

admin.site.register(models.Skill, SkillAdmin)

class ProductOwnerAdmin(admin.ModelAdmin):
    list_display = ('product_owner_id', 'first_name', 'last_name')

admin.site.register(models.ProductOwner, ProductOwnerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_owner_name', 'skill', 'description', 'min_skill_required')

    def product_owner_name(self, obj):
        return obj.product_owner.first_name + " " + obj.product_owner.last_name
    
    product_owner_name.short_description = 'Product Owner Name'

admin.site.register(models.Product, ProductAdmin)

