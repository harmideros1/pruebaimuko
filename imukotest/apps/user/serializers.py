
from .models import User
from rest_framework import serializers
from rest_framework.views import exception_handler


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                    'id',
                    'nombres',
                    'apellidos',
                    'cedula',
                    'telefono',
                    'correo',
                )