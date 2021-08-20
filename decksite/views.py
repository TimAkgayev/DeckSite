from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):
    """Home Page for DeckSite"""
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'decksite/DeckSiteMobile.html', context)
