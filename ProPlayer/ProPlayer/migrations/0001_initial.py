# Generated by Django 3.1 on 2020-12-04 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Game Title')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Team Name')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Real Name')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('birthday', models.DateField()),
                ('games', models.ManyToManyField(to='ProPlayer.Game')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProPlayer.team')),
            ],
        ),
    ]
