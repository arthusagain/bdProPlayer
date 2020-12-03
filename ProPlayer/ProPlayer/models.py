from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(verbose_name="Game Title", max_length=100)

class Team(models.Model):
    name = models.CharField(verbose_name="Team Name", max_length=100)

class Player(models.Model):
    name = models.CharField(verbose_name="Real Name", max_length=100)
    username = models.CharField(verbose_name="Username", max_length=100)
    birthday = models.DateField()
    games = models.ManyToManyField(Game)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


    



