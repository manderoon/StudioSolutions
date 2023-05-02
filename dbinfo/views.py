from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import *


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "products/product_detail.html"

class ProductOwnerListView(ListView):
    model = ProductOwner
    context_object_name = 'productowners'
    template_name = "products/product_owners.html"

class ProductOwnerDetailView(DetailView):
    model = ProductOwner
    context_object_name = 'productowner'
    template_name = "products/product_owners_detail.html"

