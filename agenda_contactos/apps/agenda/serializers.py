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