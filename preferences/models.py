from django.db import models
from products.models import Product
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class Preferences(models.Model):
    user = CurrentUserField();
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    p1 = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='first_pref');
    p2 = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='second_pref');
    p3 = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='third_pref');