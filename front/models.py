from django.db import models

# Create your models here.
class ProductosInicio (models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreImagen = models.CharField(max_length=250)
    marca = models.CharField(max_length=100)
    nombreProducto = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreImagen

class ProductosJugueteria (models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreImagen = models.CharField(max_length=250)
    marca = models.CharField(max_length=100)
    nombreProducto = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreImagen