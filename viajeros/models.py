from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, date


class AboutMe(models.Model):
    titulo = models.CharField(max_length=256)
    mi_blog = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True)


class Lugares(models.Model):
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=2500)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField("Fecha Actual(mm/dd/year)", auto_now_add=True)
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True)
  

    def __str__(self):
        return f"{self.provincia}, {self.ciudad}, {self.descripcion}, {self.autor}"


class Avatar(models.Model):
    # Va a estar asociado con el User. Avatar es una tabla anexa de User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # upload_to es la subcarpeta dentro de la carpeta media
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"

