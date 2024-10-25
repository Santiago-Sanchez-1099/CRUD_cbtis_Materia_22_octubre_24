from django.shortcuts import render
from .models import Materia
# Create your views here.
def inicio_vista(request):
    # Obtener todos los registros de la tabla Materia
    ListadoMaterias=Materia.objects.all()
    return render(request, 'gestionarMateria.html',{'lasmaterias':ListadoMaterias})