from django.forms import fields
from app_juego.models import Juego
from django import forms
from .models import Juego, JuegoPregunta
from app_preguntas.models import Respuesta

class CrearJuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = (
            "categoria",
        )

class PreguntaJugarForm(forms.ModelForm):
    class Meta:
        model = JuegoPregunta
        fields = (
            "respuesta",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #import pdb; pdb.set_trace()

        self.fields["respuesta"].queryset = queryset=Respuesta.objects.filter(pregunta=self.instance.pregunta)