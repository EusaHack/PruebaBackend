from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django.db.models import Prefetch
from .models import Contacto,Telefono
from .serializers import ContactoSerializer,ContactoListSerializer
from .pagination import ContactoPagination
# Create your views here.

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

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
        
        