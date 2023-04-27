from django.db import models
import random 

class Product(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.IntegerField(default=random.randint(1, 100))
    description = models.TextField()
    owner = models.CharField(max_length=255)
    skills = models.TextField(blank=True)
