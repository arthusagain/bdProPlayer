from django import forms
from ProPlayer.models import Player, Game, Team

class PlayerModel2Form(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
    team = forms.ModelChoiceField(queryset=Team.objects.all())

    game_options = tuple(
        [(game,game.title) for game in list(Game.objects.all())]
    )
    games = forms.MultipleChoiceField(choices=game_options, required=False)