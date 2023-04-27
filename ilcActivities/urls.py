from django.urls import path

from . import views

urlpatterns = [
    path('ilc', views.ILCHome.as_view(), name='ilc.welcome'),
]
