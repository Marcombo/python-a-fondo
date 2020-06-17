from django.db import models

# Create your models here.
from django.db import models


class Perfil(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    puede_editar = models.BooleanField()


class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=100)
    f_nacimiento = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)


class Post(models.Model):
    texto = models.CharField(max_length=1000)
    fecha = models.DateField()
    likes = models.IntegerField()
    autor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='posts')
