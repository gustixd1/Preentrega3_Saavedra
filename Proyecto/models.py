from django.db import models

# Create your models here.
class Gato(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=50)
    
class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=50)
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=50)
