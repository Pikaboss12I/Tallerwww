from tkinter import CASCADE
from django.db import models

# Create your models here.
class Alimento(models.Model):
    nombre = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=30)
    tiempo_preparacion = models.DurationField()
    categoria = models.CharField(max_length=30)

    alimento = models.ManyToManyField(Alimento)

    def __str__(self) -> str:
        return self.nombre
    