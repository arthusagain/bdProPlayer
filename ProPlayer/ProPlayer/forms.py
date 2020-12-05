from django import forms
from ProPlayer.models import Player, Game, Team

class PlayerModel2Form(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    games = forms.MultipleChoiceField(choices=list(Game.objects.all()), required=False)