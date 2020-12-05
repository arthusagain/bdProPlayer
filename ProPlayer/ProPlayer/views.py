from django.shortcuts import render
from ProPlayer.models import *
from ProPlayer.forms import *

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
            form.save().save
            return redirect('home')

    else:
        form = PlayerModel2Form

    context = {'form' : form}
    return render(request, 'accounts/register.html',context)
