from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                'placeholder':"Ingrese usuario"
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                'placeholder':"Ingrese contraseña",
                'class':"mi-clase"
            }
        )
        print(self.fields["password"].widget.attrs)


class RegisterForm(UserCreationForm):
    pass

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name"
        )