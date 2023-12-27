from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    email_dueño = models.EmailField()
    activo = models.BooleanField()

    class Meta:
        abstract = True

class Perro(Mascota):
    tamaño = models.CharField(max_length=10)
    color_de_pelo = models.CharField(max_length=15)

class Gato(Mascota):
    largo_del_pelaje = models.CharField(max_length=15)
    comportamiento = models.TextField()

