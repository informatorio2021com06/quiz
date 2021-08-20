from django.shortcuts import render

# Create your views here.
def inicio(request):
    if request.user.is_authenticated and request.user.is_staff:
        template = "app_juego/admin_dashboard.html"    
    else:
        template = "app_juego/inicio.html"
    contexto = {}
    return render(request, template, contexto)