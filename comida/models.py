from django.db import models
from django.utils import timezone

# Create your models here.


class TipoComida(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    tipocomida = models.ForeignKey(TipoComida, related_name='categoria',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Menus(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    hora_pedido = models.DateTimeField(default=timezone.now)
