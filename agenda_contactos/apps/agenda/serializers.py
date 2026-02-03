from django.db import transaction
from rest_framework import serializers
from .models import Contacto, Direccion, Telefono

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        exclude = ['contacto']
        
class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        exclude = ['contacto']   

class ContactoSerializer(serializers.ModelSerializer):
    direcciones = DireccionSerializer(many=True)
    telefonos = TelefonoSerializer(many=True)
    
    class Meta:
        model = Contacto
        fields = [
            'id',
            'nombre',
            'apellidos',
            'foto',
            'fecha_nacimiento',
            'direcciones',
            'telefonos',
        ]
        
    def validate_telefonos(self, value):
        if not value:
            raise serializers.ValidationError("Debe tener al menos un teléfono")
        return value
    
    def validate_direcciones(self, value):
        if not value:
            raise serializers.ValidationError("Debe tener al menos una dirección")
        return value
    
    @transaction.atomic    
    def create(self, validated_data):
        direcciones_data = validated_data.pop('direcciones')
        telefonos_data = validated_data.pop('telefonos')

        contacto = Contacto.objects.create(**validated_data)

        for direccion in direcciones_data:
            Direccion.objects.create(contacto=contacto, **direccion)

        for telefono in telefonos_data:
            Telefono.objects.create(contacto=contacto, **telefono)

        return contacto
    
    @transaction.atomic
    def update(self, instance, validated_data):
        direcciones_data = validated_data.pop('direcciones', None)
        telefonos_data = validated_data.pop('telefonos', None)
       
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
       
        if direcciones_data is not None:
            instance.direcciones.all().delete()
            for direccion in direcciones_data:
                Direccion.objects.create(contacto=instance, **direccion)
        
        if telefonos_data is not None:
            instance.telefonos.all().delete()
            for telefono in telefonos_data:
                Telefono.objects.create(contacto=instance, **telefono)

        return instance
    
    
class ContactoListSerializer(serializers.ModelSerializer):
    telefono = serializers.SerializerMethodField()
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model = Contacto
        fields = ["id", "nombre_completo", "telefono"]

    def get_nombre_completo(self, obj):
        return f"{obj.nombre} {obj.apellidos}".strip()

    def get_telefono(self, obj):
        tel = obj.telefonos.first()
        return tel.numero if tel else None                     