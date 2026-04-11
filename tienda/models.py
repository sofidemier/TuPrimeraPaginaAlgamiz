from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_registro = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} ({self.email})"

    def total_compras(self):
        return self.compra_set.count()

    def total_gastado(self):
        return sum(c.precio for c in self.compra_set.all())


class ClientePremium(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='premium')
    descuento = models.DecimalField(max_digits=4, decimal_places=2, default=0.10,
                                    help_text="Ej: 0.10 = 10% de descuento")
    puntos = models.PositiveIntegerField(default=0)
    nivel = models.CharField(max_length=20, choices=[
        ('plata', 'Plata'),
        ('oro', 'Oro'),
        ('platino', 'Platino'),
    ], default='plata')
    fecha_alta_premium = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Cliente Premium"
        verbose_name_plural = "Clientes Premium"

    def __str__(self):
        return f"{self.cliente.nombre} — Premium {self.get_nivel_display()}"

    def descuento_porcentaje(self):
        return int(self.descuento * 100)


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f"{self.producto} — {self.cliente.nombre} (${self.precio})"
