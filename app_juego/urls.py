from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("empezar/", views.empezar_partida, name="empezar_partida"),
    path("test_juego/<int:id>/", views.test_juego, name="ver_juego"),
    path("jugar/<int:id>/", views.jugar, name="jugar"),
    path("resultado/<int:id>/", views.resultado, name="resultado"),

    path("jugadores/", views.jugadores, name="jugadores"),
]
