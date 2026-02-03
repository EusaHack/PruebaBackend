# PruebaBackend
Este proyecto sirve de base para la generación de una agenda, haciendo uso de python y django, en la parte del backend.



Crear entorno virtual e instalar Django:
```sh
#Crear entorno virtual
python -m venv venv

#Activar entorno virtual 
venv\Scripts\activate

#Instalar Django
pip install django
```

Crear proyecto :

```sh
#Crear proyecto
django-admin startproject agenda_contactos

#Correr proyecto
python manage.py runserver

```


Crear carpeta apps :

```sh
#Crear carpeta
mkdir apps

#Crear init para reconocer apps como paquete
touch apps/__init__.py
```

Crear app y configurar app :

```sh
#Crear app
django-admin startapp agenda apps/agenda

#Configurar archivo apps.py (anadir default_auto_field y agregar "apps." en name)
default_auto_field = 'django.db.models.BigAutoField'
name = 'apps.agenda'

#Guardar cambios y hacer migraciones
python manage.py makemigrations
python manage.py migrate

```

Crear modelo Contacto en app :

```sh
#Archivo models 
class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

#Configurar para guardar las fotos en la carpeta media (dentro de senttings agregar)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

#Guardar cambios y hacer migraciones
python manage.py makemigrations
python manage.py migrate

```


Crear modelo Direccion en app :

```sh
#Crear carpeta utils con archivo estados.py 
estados = [
    ('AGS', 'Aguascalientes'),
    ('BCN', 'Baja California'),
    ('BCS', 'Baja California Sur'),
    ('CAM', 'Campeche'),
    ('CHP', 'Chiapas'),
    ('CHH', 'Chihuahua'),
    ('CMX', 'Ciudad de México'),
    ('COA', 'Coahuila'),
    ('COL', 'Colima'),
    ('DUR', 'Durango'),
    ('GUA', 'Guanajuato'),
    ('GRO', 'Guerrero'),
    ('HID', 'Hidalgo'),
    ('JAL', 'Jalisco'),
    ('MEX', 'Estado de México'),
    ('MIC', 'Michoacán'),
    ('MOR', 'Morelos'),
    ('NAY', 'Nayarit'),
    ('NLE', 'Nuevo León'),
    ('OAX', 'Oaxaca'),
    ('PUE', 'Puebla'),
    ('QUE', 'Querétaro'),
    ('ROO', 'Quintana Roo'),
    ('SLP', 'San Luis Potosí'),
    ('SIN', 'Sinaloa'),
    ('SON', 'Sonora'),
    ('TAB', 'Tabasco'),
    ('TAM', 'Tamaulipas'),
    ('TLA', 'Tlaxcala'),
    ('VER', 'Veracruz'),
    ('YUC', 'Yucatán'),
    ('ZAC', 'Zacatecas'),
]

#Archivo models
from .utils.estados import estados

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

#Guardar cambios y hacer migraciones
python manage.py makemigrations
python manage.py migrate

```


Crear modelo Telefono en app :

```sh
#Crear carpeta utils con archivo opciones.py 
opciones = [
    (1, 'Casa'),
    (2, 'Teléfono móvil'),
]

#Archivo models
from .utils.opciones import opciones

class Telefono(models.Model):
    contacto = models.ForeignKey(Contacto, related_name='telefonos', on_delete=models.CASCADE)
    tipo = models.IntegerField(max_length=50, choices=opciones)
    alias = models.CharField(max_length=255)
    numero = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.tipo} - {self.numero}" 

#Guardar cambios y hacer migraciones
python manage.py makemigrations
python manage.py migrate

```
