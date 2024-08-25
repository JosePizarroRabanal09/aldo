from django.contrib import admin
from .models import Producto
from .models import Gasto
from .models import Gasto

from .models import Capital, HistorialCapital, Gasto, Emisor, Venta, Cliente, Producto,Emisor,PagoFraccionado


@admin.register(Capital)
class CapitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'monto')
    search_fields = ('id',)

@admin.register(HistorialCapital)
class HistorialCapitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'capital', 'cantidad', 'fecha')
    list_filter = ('capital', 'fecha')
    search_fields = ('capital__id', 'cantidad')
# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria','fecha_compra', 'estado', 'precio_venta','precio_compra', 'fecha_subida')
    list_filter = ('categoria', 'estado')
    search_fields = ('nombre', 'marca', 'descripcion')

@admin.register(PagoFraccionado)
class PagoFraccionadoAdmin(admin.ModelAdmin):
    list_display = ('venta', 'monto_pagado', 'fecha_pago', 'ganancia')  # Campos que se mostrarán en la lista
    search_fields = ('venta__producto__nombre', 'venta__cliente__nombre')  # Campos para el buscador
    list_filter = ('fecha_pago',)  # Filtros en la barra lateral

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('tipo_gasto', 'monto', 'fecha', 'descripcion')
    list_filter = ('tipo_gasto', 'fecha')
    search_fields = ('tipo_gasto', 'descripcion')
    ordering = ('-fecha',)
@admin.register(Emisor)
class EmisorAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'celular', 'imagen_dni1', 'imagen_dni2')
    search_fields = ('dni', 'nombre', 'apellido')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'celular', 'dni','destino')
    search_fields = ('nombre', 'apellido', 'dni', 'celular', 'dni')


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cliente', 'fecha_compra', 'total_venta', 'pago_fraccionado', 'tipo_venta', 'estado')
    list_filter = ('tipo_venta', 'estado', 'fecha_compra')
    search_fields = ('producto__nombre', 'cliente__nombre', 'estado')
    ordering = ('-fecha_compra',)