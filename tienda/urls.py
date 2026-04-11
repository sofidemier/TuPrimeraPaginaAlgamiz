from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),

    # Clientes Premium
    path('premium/', views.lista_premium, name='lista_premium'),
    path('premium/nuevo/', views.nuevo_premium, name='nuevo_premium'),

    # Compras
    path('compras/', views.lista_compras, name='lista_compras'),
    path('compras/nueva/', views.nueva_compra, name='nueva_compra'),

    # Búsqueda
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
]
