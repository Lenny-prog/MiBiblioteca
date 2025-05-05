from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Libro
from .forms import LibroForm

@login_required
def lista_libros(request):
    libros = Libro.objects.filter(usuario=request.user)
    return render(request, 'libreria/lista_libros.html', {'libros': libros})

@login_required
def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    return render(request, 'libreria/detalle_libro.html', {'libro': libro})

@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.save(commit=False)
            nuevo_libro.usuario = request.user
            nuevo_libro.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libreria/formulario_libro.html', {'form': form})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libreria/formulario_libro.html', {'form': form})

@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libreria/confirmar_eliminar.html', {'libro': libro})