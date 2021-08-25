from django.db import models
from django.db.models.base import Model

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    consigna = models.CharField(max_length=200, blank=False, null=False)
    correcto = models.ForeignKey("Respuesta", on_delete=models.RESTRICT, related_name="responde_a", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name="preguntas", null=True)

class Respuesta(models.Model):
    valor = models.CharField(max_length=100)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="opciones")