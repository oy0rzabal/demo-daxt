from django.db import models

#Codigo para las tablas: makemigrations, migrate antes de subir la informacion
#Que hacer para que cambie con: makemigrations
#Creamos modelo Proyecto
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    imgen_proyecto= models.ImageField(upload_to='imagenes/',null=True)
    nombre_propiedad = models.CharField(max_length=255, blank=True, null=True, verbose_name='nombre propiedad')
    categoria = models.CharField(max_length=50, verbose_name='Categoría')
    codigo_interno = models.CharField(max_length=100, blank=True, null=True, verbose_name='Código Interno')
    cantidad_niveles = models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad de Niveles')
    condicion_estado = models.CharField(max_length=50, verbose_name='Condición / Estado')
    estilo = models.CharField(max_length=50, verbose_name='Estilo')
    propiedad_exclusiva = models.BooleanField(default=False, verbose_name='¿Propiedad Exclusiva?')
    propiedad_destacada = models.BooleanField(default=False, verbose_name='¿Propiedad Destacada?')
    # Ubicación
    pais = models.CharField(max_length=100, verbose_name='País')
    estado_provincia = models.CharField(max_length=100, verbose_name='Estado/ Provincia')
    ciudad_delegacion = models.CharField(max_length=100, verbose_name='Ciudad/ Delegación')
    direccion1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección 1')
    direccion2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección 2')
    # Comisión del Proyecto
    monto_venta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name='Monto de Venta')
    monto_brokers = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Monto Para Brokers')
    # Características del Inmueble
    facilidades_comunes = models.JSONField(blank=True, null=True, verbose_name='Facilidades Comunes')
    facilidades_electricas = models.JSONField(blank=True, null=True, verbose_name='Facilidades Eléctricas')
    exterior = models.JSONField(blank=True, null=True, verbose_name='Exterior')
    general = models.JSONField(blank=True, null=True, verbose_name='General')
    interior = models.JSONField(blank=True, null=True, verbose_name='Interior')
    politicas = models.JSONField(blank=True, null=True, verbose_name='Políticas')
    ubicacion = models.JSONField(blank=True, null=True, verbose_name='Ubicación')
    construccion = models.JSONField(blank=True, null=True, verbose_name='Construcción')

    def __str__(self):
        return self.nombre_propiedad
