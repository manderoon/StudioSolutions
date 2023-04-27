from django.shortcuts import render

from django.views.generic import TemplateView
from django.views import View

from datetime import datetime


class StudioWelcomeView(TemplateView):
    template_name = 'home/studiowelcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate season based on current month
        current_month = datetime.now().month
        if current_month in [1, 2, 3, 4, 5, 6, 7]:
            season = "Autumn"
        else:
            season = "Spring"

        context['today'] = datetime.today()
        context['year'] = datetime.now().year
        context['season'] = season

        return context
    

class AboutView(View):
    def get(self, request):
        # Logic for handling GET request
        context = {
            'page_title': 'About Us',
            'page_content': 'This is the about page of our website.',
        }
        return render(request, 'home/about.html', context)
    



