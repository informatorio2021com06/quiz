from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("categorias/", views.categorias, name="categorias"),
    path("categorias/add/", views.add_categoria, name="add_categoria"),
    path("categorias/<int:id>/", views.show_categoria, name="show_categoria"),
    path("categorias/<int:id>/edit/", views.edit_categoria, name="edit_categoria"),
    path("categorias/<int:id>/delete/", views.delete_categoria, name="delete_categoria"),

    path("preguntas/", views.preguntas, name="preguntas"),
    path("preguntas/add/", views.add_pregunta, name="add_pregunta"),
    path("preguntas/<int:id>/", views.show_pregunta, name="show_pregunta"),
    # path("preguntas/<int:id>/edit/", views.edit_pregunta, name="edit_pregunta"),
    # path("preguntas/<int:id>/delete/", views.delete_pregunta, name="delete_pregunta"),    
]
