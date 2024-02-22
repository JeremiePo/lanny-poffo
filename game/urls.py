from django.urls import path
from .games.RandomWrestler import RandomWrestler
from .games.playAI import PlayAI
from . import views

urlpatterns = [
    path("/randomizer/", RandomWrestler.as_view(), name="radomWrestler"),
    path("/play/", PlayAI.as_view(), name="play")
]
