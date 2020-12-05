from django.shortcuts import render
from ProPlayer.models import *

# Create your views here.

def home(request):
    allPlayers = Player.objects.all()
    context = {
        'players':allPlayers,
    }
    return render(request,"ProPlayer/home.html",context)
