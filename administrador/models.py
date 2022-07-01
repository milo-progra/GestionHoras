from pickle import TRUE
from django.db import models
from django.forms import CharField

# Create your models here.
class Servicio (models.Model):

    id_servicio = models.AutoField(primary_key=TRUE)
    nombre = models.CharField( null=False, max_length=50)
    precio = models.IntegerField(null=False)


    def __str__(self):
        return self.nombre


