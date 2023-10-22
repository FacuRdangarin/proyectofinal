from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()
    def __str__(self):
        return f"nombre: {self.curso} - Camada {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField() 
    def __str__(self):
        return f"Nombre: {self.nombre} - fecha_de_entrega {self.fecha_de_entrega} - Entregado {self.entregado}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    
    def __str__(self):
       return f"{self.user}{self.imagen}"
   
class Blog(models.Model):
    titulo = models.CharField(max_length=15)
    subTitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=300)
    autor = models.CharField (max_length=20)
    fecha = models.DateTimeField()
    foto = models.ImageField()