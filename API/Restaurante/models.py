from django.db import models
from tkinter import CASCADE

# Create your models here.
class Alimento(models.Model):
    nombre = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    def str(self) -> str:
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=30)
    tiempo_preparacion = models.DurationField()
    categoria = models.CharField(max_length=30)
    alimento = models.ManyToManyField(Alimento)

    def str(self) -> str:
        return self.nombre

# Create your models here.
