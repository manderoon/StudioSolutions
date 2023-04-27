from django.urls import path

from . import views

urlpatterns = [
    # app and any parameters pass in, the function name in views 
    path('preferencesview', views.preferences_view, name="preferencesview"),
]