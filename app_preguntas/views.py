from app_preguntas.forms import CategoriaForm, PreguntaForm
from django.http import request
from django.shortcuts import redirect, render
from .models import Categoria, Pregunta, Respuesta

from django.contrib.auth.decorators import login_required, user_passes_test

def user_is_staff(user):
    return user.is_staff or user.is_superuser

# Create your views here.
@login_required
@user_passes_test(user_is_staff)
def categorias(request):
    categorias = Categoria.objects.all()
    template = "app_preguntas/categorias.html"
    contexto = {
        "categorias":categorias
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(user_is_staff)
def add_categoria(request):
    form = CategoriaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            cat = form.save()
            return redirect("categorias")

    template = "app_preguntas/add_categoria.html"
    contexto = {
        "form":form
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(user_is_staff)
def edit_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)

    form = CategoriaForm(request.POST or None, instance=categoria)
    
    if request.method == "POST":
        if form.is_valid():
            cat = form.save()
            return redirect("categorias")
            
    template = "app_preguntas/add_categoria.html"
    contexto = {
        "form":form
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(user_is_staff)
def show_categoria(request, id):
    cat = Categoria.objects.get(pk=id)
    template = "app_preguntas/categoria.html"
    contexto = {
        "cat":cat
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(user_is_staff)
def delete_categoria(request,id):
    cat = Categoria.objects.get(pk=id)
    if request.method == "POST":
        cat.delete()
        return redirect("categorias")
    template = "app_preguntas/delete_categoria.html"
    contexto = {
        "cat":cat
    }
    return render(request,template,contexto)
    



@login_required
@user_passes_test(user_is_staff)
def add_pregunta(request):
    form = PreguntaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            consigna = form.cleaned_data["consigna"]
            categoria = form.cleaned_data["categoria"]
            respuesta_correcta = form.cleaned_data["respuesta_correcta"]
            respuesta_2 = form.cleaned_data["respuesta_2"]
            respuesta_3 = form.cleaned_data["respuesta_3"]

            pregunta = Pregunta(
                consigna = consigna,
                categoria = categoria
            )
            pregunta.save()

            resp_correcta = Respuesta(
                valor = respuesta_correcta,
                pregunta = pregunta
            )
            resp_correcta.save()
            pregunta.correcto = resp_correcta
            pregunta.save()

            resp_2 = Respuesta(
                valor = respuesta_2,
                pregunta = pregunta
            )
            resp_3 = Respuesta(
                valor = respuesta_3,
                pregunta = pregunta
            )
            resp_2.save()
            resp_3.save()

            return redirect("show_pregunta", pregunta.id)

    template = "app_preguntas/add_pregunta.html"
    contexto = {
        "form":form
    }
    return render(request, template, contexto)


@login_required
@user_passes_test(user_is_staff)
def show_pregunta(request, id):
    pregunta = Pregunta.objects.get(pk=id)
    template = "app_preguntas/pregunta.html"
    contexto = {
        "pregunta":pregunta
    }
    return render(request, template, contexto)

@login_required
@user_passes_test(user_is_staff)
def preguntas(request):
    preguntas = Pregunta.objects.all()
    template = "app_preguntas/preguntas.html"
    contexto = {
        "preguntas":preguntas
    }
    return render(request, template, contexto)    