from django.urls import path

from . import views

urlpatterns = [
    path('home', views.StudioWelcomeView.as_view(), name='studio.welcome'),
    path('about/', views.AboutView.as_view(), name='about'),
    
]
