from django.shortcuts import render
from ProPlayer.models import Player 


# Create your views here.

def home(request):
    return render(request,"ProPlayer/home.html")