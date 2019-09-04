from django.contrib import admin
from .models import User

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    list_display = (
                    'id',
                    'nombres',
                    'apellidos',
                    'cedula',
                    'telefono',
                    'correo',
                    'full_name'
                )
