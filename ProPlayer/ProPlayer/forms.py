from django import forms
from ProPlayer.models import Player, Game, Team

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return obj.name

class PlayerModel2Form(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

    team = CustomModelChoiceField(queryset=None)

    game_options = lambda  : tuple(
        [(game.pk,game.title) for game in list(Game.objects.all())]
    )
    games = forms.MultipleChoiceField(choices=game_options, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.all()
        

class GameModel2Form(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class TeamModel2Form(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'