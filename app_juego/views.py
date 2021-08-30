from app_preguntas.models import Pregunta
from django.shortcuts import redirect, render
from .forms import CrearJuegoForm, PreguntaJugarForm
from .models import Categoria, Juego, JuegoPregunta
from django.contrib.auth.models import User
# Create your views here.
def inicio(request):
    contexto = {}
    if request.user.is_authenticated and request.user.is_staff:
        template = "app_juego/admin_dashboard.html"    
    else:
        template = "app_juego/inicio.html"
        form = CrearJuegoForm()
        contexto.update({
            "form":form
        })
    return render(request, template, contexto)

def empezar_partida(request):
    if not request.method == "POST":
        return redirect("inicio")
    print("\n\ncrear form")
    form = CrearJuegoForm(request.POST)
    print("\n\ndespues de crear form")

    if form.is_valid():
        try:
            juego = form.save(commit=False)
            juego.participante = request.user
            juego.save()
            preguntas = Pregunta.objects.filter(categoria = juego.categoria ).order_by("?")[:5]
            for preg in preguntas:
                juego.detalle_respuestas.create(pregunta = preg, estado = JuegoPregunta.ESTADO_CHOICES[0])
        except Exception as ex:
            print(ex)
            return redirect("inicio")
        return redirect("jugar", juego.id)
    else:
        print("form no válido.")
        print(form.errors)
        return redirect("inicio")

def test_juego(request, id):
    juego = Juego.objects.get(pk=id)
    contexto = {
        "juego":juego
    }
    template = "app_juego/prueba_juego.html"
    return render(request,template,contexto)

def jugar(request, id):
    juego = Juego.objects.get(pk=id)
    lista_detalle_juego = juego.detalle_respuestas.filter(estado=JuegoPregunta.ESTADO_CHOICES[0])
 
    if lista_detalle_juego:
        detalle_juego = lista_detalle_juego[0]
        pregunta = detalle_juego.pregunta
        form = PreguntaJugarForm(request.POST or None,instance=detalle_juego)
    else:
        return redirect("resultado", juego.id)
    print("pregunta: ", detalle_juego.pregunta, detalle_juego.estado)
    if request.method == "POST":
        if form.is_valid():
            print("valido")
            respuesta = form.cleaned_data["respuesta"]
            detalle_juego.respuesta = respuesta
            if detalle_juego.respuesta == pregunta.correcto:
                detalle_juego.estado = JuegoPregunta.ESTADO_CHOICES[1]
            else:
                detalle_juego.estado = JuegoPregunta.ESTADO_CHOICES[2]
            detalle_juego.save()
            return redirect("jugar", juego.id)


    contexto = {
        "juego":juego,
        "pregunta":pregunta,
        "form":form
    }
    template = "app_juego/pregunta.html"
    return render(request,template,contexto)

def resultado(request, id):
    juego = Juego.objects.get(pk=id)
    template = "app_juego/resultado.html"
    contexto = {
        "juego":juego
    }
    return render(request,template,contexto)


def jugadores(request):
    perfiles = User.objects.all()
    contexto = {
        "perfiles":perfiles
    }
    return render(request,"app_juego/jugadores.html", contexto)