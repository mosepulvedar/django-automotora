from django.db import models

# Create your models here.


class Marca(models.Model):
    #django agrega un id a todos los modelos (autoincrementable)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Automovil(models.Model):
    pantente = models.CharField(max_length=10, unique=True, verbose_name="Patente")
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name='año')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.pantente

    class Meta:
        verbose_name = "Automovil"
        verbose_name_plural = "Automoviles"
