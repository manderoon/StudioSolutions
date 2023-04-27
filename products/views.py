from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "products/product_detail.html"

