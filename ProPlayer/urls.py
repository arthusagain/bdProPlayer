"""ProPlayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.edit import UpdateView
from . import views
from ProPlayer.models import Player
from django.urls.base import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('', views.home, name='home'),

    path('add-player/', views.add_player, name='add-player'),
    path('edit-player/<int:pk>/', views.edit_player, name='edit-player'),
    path('rm-player/<int:pk>/', views.remove_player, name='rm-player'),

    path('add-game/', views.add_game, name='add-game'),
    path('add-team/', views.add_team, name='add-team'),
]
