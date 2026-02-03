from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"