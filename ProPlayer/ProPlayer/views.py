from django.shortcuts import render
from ProPlayer.models import *
from ProPlayer.forms import *
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

def home(request):
    allPlayers = Player.objects.all()
    context = {
        'players':allPlayers,
    }
    return render(request,"ProPlayer/home.html",context)



def add_player(request):
    if request.method == 'POST':
        form = PlayerModel2Form(request.POST)
        if form.is_valid():
            form.save().save()
            return HttpResponseRedirect(reverse_lazy('home'))

    else:
        form = PlayerModel2Form

    context = {'form' : form}
    return render(request, 'ProPlayer/player-form.html',context)

def add_game(request):
    if request.method == 'POST':
        form = GameModel2Form(request.POST)
        if form.is_valid():
            form.save().save()
            return HttpResponseRedirect(reverse_lazy('home'))

    else:
        form = GameModel2Form

    context = {'form' : form}
    return render(request, 'ProPlayer/game-form.html',context)

def add_team(request):
    if request.method == 'POST':
        form = TeamModel2Form(request.POST)
        if form.is_valid():
            form.save().save()
            return HttpResponseRedirect(reverse_lazy('home'))

    else:
        form = TeamModel2Form

    context = {'form' : form}
    return render(request, 'ProPlayer/team-form.html',context)
