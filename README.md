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
