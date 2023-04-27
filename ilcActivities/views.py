from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.views.generic import TemplateView
from django.views import View



class ILCHome(TemplateView):
    template_name = 'ilcActivities/ilcHome.html'