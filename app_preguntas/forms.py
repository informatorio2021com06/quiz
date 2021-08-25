from django import forms
from django.forms import fields
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update({
            "placeholder":"Titulo de la categoria"
        })
        self.fields["descripcion"].widget.attrs.update({
            "placeholder":"Descripcion de la categoria"
        })

class PreguntaForm(forms.Form):
    consigna = forms.CharField(max_length=200, required=True)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    respuesta_correcta = forms.CharField(max_length=100,required=True)
    respuesta_2 = forms.CharField(max_length=100,required=True)
    respuesta_3 = forms.CharField(max_length=100,required=True)