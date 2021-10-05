from django.db import models


class Rama(models.Model):
    nombre = models.CharField(max_length=100)
    rama = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'El nombre es <<%s>>, la rama es <<%s>>' % (self.nombre, self.rama)


class Hoja(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    formula = models.CharField(max_length=500)
    propiedades = models.CharField(max_length=500)
