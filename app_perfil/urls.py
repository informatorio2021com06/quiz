from django.contrib.auth import logout, views as auth_views
from django.urls import path, include, reverse_lazy
from . import views
from .forms import LoginForm
from django.views import View
urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name = "app_perfil/login.html",
            form_class = LoginForm
        ),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        "register/",
        views.register,
        name="register"
    ),
    path("<int:id>/", views.perfil, name="perfil"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path(
        "password/",
        auth_views.PasswordChangeView.as_view(
            template_name = "app_perfil/password.html",
            success_url = reverse_lazy("inicio")
        ),
        name="change_password"
    ),    

]