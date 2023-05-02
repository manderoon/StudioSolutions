from django.urls import path

from . import views

urlpatterns = [
    # app and any parameters pass in, the function name in views 
    path('products', views.ProductListView.as_view(), name="products.list"),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name="products.detail"),
    path('productsowners', views.ProductOwnerListView.as_view(), name="productsowners.list"),
    path('productsowners/<int:pk>', views.ProductOwnerDetailView.as_view(), name="productsowners.detail"),

]