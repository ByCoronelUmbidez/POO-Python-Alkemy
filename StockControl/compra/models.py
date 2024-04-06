from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.IntegerField()
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.FloatField(max_length=100)
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre



