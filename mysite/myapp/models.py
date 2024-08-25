from django.db import models
from django.utils import timezone

class Gasto(models.Model):
    TIPO_GASTO = [
        ('Pasaje', 'Pasaje'),
        ('Comida', 'Comida'),
        ('Otros', 'Otros'),
    ]
    tipo_gasto = models.CharField(max_length=50, choices=TIPO_GASTO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.TextField()
    eliminado = models.BooleanField(default=False)  # Nuevo campo para eliminación lógica

    def __str__(self):
        return f"{self.tipo_gasto} - {self.monto} - {self.fecha}"


class PagoFraccionado(models.Model):
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, related_name='pagos')
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(default=timezone.now)
    ganancia = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Nuevo campo de ganancia


class Capital(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def aumentar_capital(self, cantidad):
        self.monto += cantidad
        self.save()
        # Almacenar en el historial
        HistorialCapital.objects.create(capital=self, cantidad=cantidad, fecha=timezone.now())

class HistorialCapital(models.Model):
    capital = models.ForeignKey(Capital, on_delete=models.CASCADE, related_name='historiales')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Aumento de {self.cantidad} el {self.fecha}"

class Emisor(models.Model):
    dni = models.CharField(max_length=8)
    imagen_dni1 = models.ImageField(upload_to='dni_images/', blank=True, null=True)
    imagen_dni2 = models.ImageField(upload_to='dni_images/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    eliminado = models.BooleanField(default=False)  # Nuevo campo para eliminación lógica

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.dni}"

class Venta(models.Model):
    TIPO_VENTA_CHOICES = [
        ('NORMAL', 'Normal'),
        ('FRACCIONADO', 'Fraccionado'),
        ('DROPSHIPPING', 'Dropshipping'),
    ]

    ESTADO_VENTA_CHOICES = [
        ('COMPLETADO', 'Completado'),
        ('PENDIENTE', 'Pendiente'),
    ]

    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField()  # Removido auto_now_add=True
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Cambiado a default=0
    pago_fraccionado=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tipo_venta = models.CharField(max_length=20, choices=TIPO_VENTA_CHOICES, default='NORMAL')
    estado = models.CharField(max_length=20, choices=ESTADO_VENTA_CHOICES, default='COMPLETADO')
    eliminado = models.BooleanField(default=False)  # Nuevo campo para eliminación lógica

    def __str__(self):
        return f"Venta {self.id} - {self.producto.nombre} a {self.cliente.nombre} en {self.fecha_compra} - {self.tipo_venta} - {self.estado}"
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    dni = models.CharField(max_length=8)
    destino = models.CharField(max_length=20)
    eliminado = models.BooleanField(default=False)  # Nuevo campo para eliminación lógica

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    CATEGORIAS = [
        ('Zapatilla', 'Zapatilla'),
        ('Polo', 'Polo'),
        ('Mochila', 'Mochila'),
    ]

    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Separado', 'Separado'),
        ('Vendido', 'Vendido'),
    ]

    nombre = models.CharField(max_length=100)
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='Disponible')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    eliminado = models.BooleanField(default=False)  # Nuevo campo para eliminación lógica

    def __str__(self):
        return self.nombre