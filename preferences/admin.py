from django.contrib import admin
from . import models

# Register your models here.
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(models.Preferences, PreferencesAdmin)

