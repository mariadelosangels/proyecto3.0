from django.urls import path
from .views import agregar_perro, agregar_gato, buscar_mascotas, lista_mascotas

urlpatterns = [
    path('agregar_perro/', agregar_perro, name='agregar_perro'),
    path('agregar_gato/', agregar_gato, name='agregar_gato'),
    path('buscar_mascotas/', buscar_mascotas, name='buscar_mascotas'),
    path('lista_mascotas/', lista_mascotas, name='lista_mascotas'),  # Ajusta según tu configuración
    # Otras rutas de URL para otras vistas o funcionalidades
]