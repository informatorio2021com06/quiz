from django.shortcuts import redirect, render
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return redirect("login")
    contexto = {
        "form":form
    }
    return render(
        request,
        "app_perfil/register.html",
        contexto
    )

def perfil(request, id):
    #user = get_user_model().objects.get(pk=id)
    user = User.objects.get(pk=id)
    contexto = {
        "usuario":user
    }
    return render(request, "app_perfil/perfil.html", contexto)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("iniciar_sesion")

    perfil = request.user
    form = EditProfileForm(instance=perfil)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=perfil)
        if form.is_valid():
            user = form.save()
            return redirect("inicio")
    contexto = {"form":form}
    return render(request, "app_perfil/edit.html",contexto)