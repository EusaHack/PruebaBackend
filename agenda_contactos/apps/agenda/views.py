from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django.db.models import Prefetch
from .models import Contacto,Telefono
from .serializers import ContactoSerializer,ContactoListSerializer,DireccionSerializer, TelefonoSerializer
from .pagination import ContactoPagination
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    
    @action(detail=True, methods=["get"], url_path="direcciones")
    def direcciones(self, request, pk=None):
        contacto = self.get_object()
        serializer = DireccionSerializer(contacto.direcciones.all(), many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["get"], url_path="telefonos")
    def telefonos(self, request, pk=None):
        contacto = self.get_object()
        serializer = TelefonoSerializer(contacto.telefonos.all(), many=True)
        return Response(serializer.data)

class ContactoListadoPaginadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contacto.objects.all().order_by("id")
    serializer_class = ContactoListSerializer
    pagination_class = ContactoPagination    
    
class ContactoListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactoListSerializer
    filter_backends = [SearchFilter]
    search_fields = ["nombre", "apellidos", "telefonos__numero"]

    def get_queryset(self):
        return (
            Contacto.objects.all()
            .prefetch_related(
                Prefetch("telefonos", queryset=Telefono.objects.order_by("id"))
            )
            .order_by("id")
            .distinct()
        )    
        
        