from django.db import models
from datetime import date


class Usuario(models.Model):
    usuario = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    contraseña = models.CharField(max_length=30, blank=False, null=False,)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    dirección = models.CharField(max_length=100, blank=False, null=False)
    lugar = models.CharField(max_length=50, blank=False, null=False)
    teléfono = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.usuario

class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripción = models.TextField(max_length=500, blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    imagen = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre

class Orden(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha

opciones_consultas= [
    [0,'Consulta'],
    [1,'Reclamo'],
    [2,'Sugerencia'],
    [3,'Felicitaciones'],
]

class Contactenos(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100, blank=False, null=False)
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()

    def __str__(self):
        return self.nombre