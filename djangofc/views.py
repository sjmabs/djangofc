from django.shortcuts import render

from .models import Player

# Create your views here.
def index(request):
    context = {}
    return render(request, 'djangofc/index.html', context)

def about(request):
    context = {}
    return render(request, 'djangofc/about.html', context)

def team(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'djangofc/team.html', context)
