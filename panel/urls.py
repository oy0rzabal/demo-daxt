from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    #Urls de Registro:
    path('clientes', views.clientes, name='clientes'),
    path('clientes/crear', views.crear_cliente, name='crear'),


    #REGISTRO DE PROYCTOS:
    path('proyectos', views.proyect, name='proyectos'),
    path('guardar/', views.guardar_proyecto, name='guardar_proyecto'),
    path('proyectos/detalles/<int:pk>/', views.mostrar_proyecto, name='mostrar_proyecto'),
    path('proyecto/editar', views.proyecto_editar, name='proyecto_editar'),
    path('proyecto/borrar', views.proyecto_borrar, name='proyecto_borrar'),


    #URL para estudio de trrenos
    path('terreno', views.estudio_terreno, name='estudio'),

    #EstudioTecnico
    path('tecnico', views.estudio_tecnico, name='tecnico'),
    path('tecnico/crear', views.crear_tecnico, name='crear_tecnico'),
]
