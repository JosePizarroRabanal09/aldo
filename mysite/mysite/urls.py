
from django.contrib import admin
from django.urls import path
from myapp.views  import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('', home, name='home'),  # Ruta para la vista home
    path('salir/', salir_view, name='salir'),
    path('perfil/', perfil_view, name='perfil'),
    path('crear-cliente/', crear_cliente, name='crear_cliente'),
    path('ventas/', ver_ventas, name='ver_ventas'),
    path('gastos/', crear_gasto, name='crear_gasto'),
    path('crear-producto/', crear_producto, name='crear_producto'),
    path('ver_clientes/', ver_clientes, name='ver_clientes'),
    path('ver_productos/', ver_productos, name='ver_productos'),
    path('ver_gastos/', ver_gastos, name='ver_gastos'),
    path('ver_ventas/', ver_ventas, name='ver_ventas'),
    path('ver_dropshipping/', ver_dropshipping, name='ver_dropshipping'),
    path('ventas/crear/', crear_venta, name='crear_venta'),
    path('agregar_pago/', agregar_pago, name='agregar_pago'),
    path('emisores/', listar_emisores, name='listar_emisores'),
    path('agregar-emisor/', agregar_emisor, name='agregar_emisor'),
    path('declaracion_jurada/', declaracion_jurada, name='declaracion_jurada'),
    path('aumentar_capital/', aumentar_capital, name='aumentar_capital'),
    path('reportes/', ver_reportes, name='ver_reportes'),

]
