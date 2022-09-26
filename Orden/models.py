import datetime
from django.db import models
from django.contrib.auth import get_user_model
from modelos.models import Producto

Usuario = get_user_model()

opciones_lugar = [
    [0, 'Bogota'],
    [1, 'Mosquera'],
    [2, 'Tena'],
    [3, 'La Gran via'],
    [4, 'La Mesa'],
    [5, 'San javier']
]

class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=100, verbose_name='dirección', blank=True)
    lugar = models.IntegerField(choices=opciones_lugar, default=0)
    telefono = models.CharField(max_length=10, blank=True)
    fecha = models.DateTimeField(default=datetime.datetime.now)
    total = models.IntegerField(null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return 'Orden N°{}'.format(self.id)


class CompraItem(models.Model):
    compra = models.ForeignKey(Compra, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='compra_items', on_delete=models.DO_NOTHING)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'




