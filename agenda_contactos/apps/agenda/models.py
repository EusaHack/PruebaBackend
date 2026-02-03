from django.db import models
from .utils.estados import estados

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Direccion(models.Model):
    contacto = models.ForeignKey(Contacto, related_name='direcciones', on_delete=models.CASCADE)
    calle = models.CharField(max_length=255)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10)
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=3 , choices=estados)
    referencias = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.municipio}, {self.estado}"    