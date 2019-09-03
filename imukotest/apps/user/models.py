import uuid
from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    # cedula = models.CharField(max_length=11, unique=True)
    cedula = models.DecimalField(max_digits=11, decimal_places=0)
    # telefono = models.CharField(max_length=20)
    telefono = models.DecimalField(max_digits=11, decimal_places=0)
    correo = models.EmailField(unique=True)


    def clean(self):
        pass
        # Se que no fue la mejor forma de validar los numeros de telefono y cedula,
        # Pero no me funcionaron los REGEX


    def __str__(self):
        return self.nombres + " " + self.apellidos

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
