

from django.shortcuts import render, redirect
from .forms import PerroForm, GatoForm, BuscarForm
from .models import Perro, Gato

def agregar_perro(request):
    if request.method == 'POST':
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')  # Ajusta la URL de redirección según tu configuración
    else:
        form = PerroForm()
    
    return render(request, 'agregar_perro.html', {'form': form})

def agregar_gato(request):
    if request.method == 'POST':
        form = GatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')  # Ajusta la URL de redirección según tu configuración
    else:
        form = GatoForm()
    
    return render(request, 'agregar_gato.html', {'form': form})

def buscar_mascotas(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino_de_busqueda']
            perros = Perro.objects.filter(nombre__icontains=termino)
            gatos = Gato.objects.filter(nombre__icontains=termino)
            return render(request, 'resultados_busqueda.html', {'perros': perros, 'gatos': gatos})
    else:
        form = BuscarForm()

    return render(request, 'buscar_mascotas.html', {'form': form})