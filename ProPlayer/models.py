from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(verbose_name="Game Title", max_length=100)

class Team(models.Model):
    name = models.CharField(verbose_name="Team Name", max_length=100)

class Player(models.Model):
    name = models.CharField(verbose_name="Real Name", help_text='Entre o nome', max_length=100)
    username = models.CharField(verbose_name="Username", help_text='Entre o nome de usuário', max_length=100)
    birthday = models.DateField(help_text='Entre a data de aniversário')
    games = models.ManyToManyField(Game, help_text='Entre os jogos jogados')
    team = models.ForeignKey(Team, help_text='Entre o time', on_delete=models.CASCADE)
    matches = models.IntegerField(help_text='Entre o numero de partidas')
    victories = models.IntegerField(help_text='Entre o numero de vitorias')

    



