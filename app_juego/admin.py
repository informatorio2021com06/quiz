from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class PerfilAdmin(UserAdmin):
    # search_fields = ['username', 'first_name', 'last_name']
    list_display = [
    'username', 'first_name',
     'last_name',
     'is_staff', 'is_superuser', 'last_login']

    fieldsets = (
        ('Usuario',
            {'fields': ('username', 'password')}),
        ('Información Personal',
            {'fields': (
                'first_name',
                'last_name',
                'email',

            )}),
        ("otros datos",
            {'fields':(
                'birthday',
            )}),
        ('Permisos',
            {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',

        )}),
    )
admin.site.unregister(User)
admin.site.register(User, PerfilAdmin)