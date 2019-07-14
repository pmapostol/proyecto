from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    rol = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField()
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    
    def __str__(self):
        return self.nombre



class Ubicacion(models.Model):
    sede = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    piso = models.IntegerField()
    estante = models.CharField(max_length=50)

    def __str__(self):
        return self.sede



class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    escuela = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tesi(models.Model):
    nombre = models.CharField(max_length=50)
    autor_1 = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='autor_1') 
    autor_2 = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='autor_2') 
    tutor = models.CharField(max_length=50)
    jurado1 = models.CharField(max_length=50)
    jurado2 = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    resumen = models.CharField(max_length=200)
    calificacion = models.FloatField()
    fecha_creacion = models.DateTimeField()
    estatus = models.CharField(max_length=50)
    escuela = models.CharField(max_length=50)
    palabra_clave = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

