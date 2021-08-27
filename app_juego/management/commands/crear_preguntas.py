from django.core.management import BaseCommand
from app_preguntas.models import Categoria,Pregunta, Respuesta

from csv import DictReader

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("./categorias.csv", 'r') as archivo:
            for fila in DictReader(archivo):
                cat = Categoria()
                cat.nombre = fila["nombre"]
                cat.descripcion = fila["descripcion"]
                cat.save()

        with open("./preguntas.csv", 'r') as archivo:
            for fila in DictReader(archivo):
                preg = Pregunta()
                resp_correcta = Respuesta()
                resp_2 = Respuesta()
                resp_3 = Respuesta()
                categoria = Categoria.objects.filter(nombre=fila["categoria"])[0]

                preg.consigna = fila["consigna"]
                preg.categoria = categoria
                preg.save()

                resp_correcta.valor = fila["correcto"]
                resp_correcta.pregunta = preg
                resp_correcta.save()

                preg.correcto = resp_correcta

                resp_2.valor = fila["resp2"]
                resp_3.valor = fila["resp3"]
                resp_2.pregunta = preg
                resp_3.pregunta = preg
                resp_2.save()
                resp_3.save()


            # fila["categoria"]
            # fila["consgina"]
            # fila["correcto"]
            # fila["resp2"]
            # fila["resp1"]