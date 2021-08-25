from app_preguntas.models import Categoria, Pregunta, Respuesta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Juego(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, null=True)
    participante = models.ForeignKey(User, on_delete=models.CASCADE)
    preguntas = models.ManyToManyField(Pregunta, through="JuegoPregunta")

class JuegoPregunta(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name="detalle_respuestas")
    pregunta = models.ForeignKey(Pregunta, on_delete=models.RESTRICT, related_name="detalle_respuestas")
    respuesta = models.ForeignKey(Respuesta, on_delete=models.RESTRICT)
    ESTADO_CHOICES = (
        ("in_progress", "En Progreso"),
        ("correct", "Correcto"),
        ("incorrect", "Incorrecto"),
        ('ended', "Finalizado")
    )
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, null=False, default="in_progress")