from django.contrib import admin
from .models import Producto
from .models import Gasto
from .models import Gasto
from .models import Capital, HistorialCapital, Gasto, Emisor, Venta, Cliente, Producto

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
    list_display = ('nombre', 'categoria', 'estado', 'precio_venta','precio_compra', 'fecha_subida')
    list_filter = ('categoria', 'estado')
    search_fields = ('nombre', 'marca', 'descripcion')



@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('tipo_gasto', 'monto', 'fecha', 'descripcion')
    list_filter = ('tipo_gasto', 'fecha')
    search_fields = ('tipo_gasto', 'descripcion')
    ordering = ('-fecha',)