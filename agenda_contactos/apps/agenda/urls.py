from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactoViewSet,ContactoListViewSet,ContactoListadoPaginadoViewSet

router = DefaultRouter()
router.register(r'contactos', ContactoViewSet, basename='contactos')
router.register(r'contactos-list', ContactoListViewSet, basename='contactos-list')
router.register(r'contactos-paginado', ContactoListadoPaginadoViewSet, basename='contactos-paginado')
urlpatterns = [
    path('', include(router.urls)),
]