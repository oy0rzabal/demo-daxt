from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")



##Modulo Registro_Clintes
def clientes(request):
    return render(request, 'registro_clientes/Clientes.html')
def crear_cliente(request):
    return render(request, 'registro_clientes/crear.html') #Creamos la conexion del boton en views clientes


#Modulo de Gerencia de Proyectos:
#Agregar nuevo proyecto:
def proyect(request):
    return render(request, 'proyecto/proyecto.html')

def guardar_proyecto(request):
    if request.method == 'POST':
        form = Proyecto(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save()
            return redirect('proyecto/mostrar_proyecto.html', pk=proyecto.pk)  # Redirige a la vista que muestra los datos guardados
    else:
        form = Proyecto()
    return render(request, 'proyecto/ProyectoForm.html', {'form': form})

def mostrar_proyecto(request, pk):
    proyecto = Proyecto.objects.get(pk=pk)
    return render(request, 'mostrar_proyecto.html', {'proyecto': proyecto})

def proyecto_editar(request):
    return render(request, 'proyecto/proyecto_editar.html')
def proyecto_borrar(request):
    return render(request, 'proyecto/proyecto_borrar.html')

#Estudio de Terreno
def estudio_terreno(request):
    return render(request, 'estudio_terrenos/terreno.html')

#ModuloTecnico
def estudio_tecnico(request):
    return render(request, 'estudio_tecnico/estudio.html')
def crear_tecnico(request):
    return render(request, 'estudio_tecnico/crear_estudio.html')