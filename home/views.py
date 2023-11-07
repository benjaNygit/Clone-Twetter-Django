from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    """Vista Home
    Página de inicio del sitio web
    """
    template_name = "index.html"
