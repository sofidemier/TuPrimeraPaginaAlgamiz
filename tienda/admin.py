from django.contrib import admin
from .models import Cliente, ClientePremium, Compra


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'saldo', 'fecha_registro']
    search_fields = ['nombre', 'email']
    list_filter = ['fecha_registro']
    ordering = ['-fecha_registro']


@admin.register(ClientePremium)
class ClientePremiumAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'nivel', 'descuento', 'puntos', 'fecha_alta_premium']
    list_filter = ['nivel']
    search_fields = ['cliente__nombre', 'cliente__email']


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cliente', 'precio', 'fecha']
    search_fields = ['producto', 'cliente__nombre']
    list_filter = ['fecha']
    ordering = ['-fecha']
