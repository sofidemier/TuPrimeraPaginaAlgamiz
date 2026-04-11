"""
Script para poblar la base de datos con datos de prueba.
Correr con: python populate_db.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuprimerapage.settings')
django.setup()

from django.contrib.auth.models import User
from tienda.models import Cliente, ClientePremium, Compra

# Superusuario
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@clientehub.com', 'admin1234')
    print("✅ Superusuario creado → usuario: admin | contraseña: admin1234")

# Clientes de prueba
clientes_data = [
    {"nombre": "Ana García",    "email": "ana@email.com",    "direccion": "Av. Corrientes 1234, CABA",    "telefono": "11-2345-6789", "saldo": 5000.00},
    {"nombre": "Luis Pérez",    "email": "luis@email.com",   "direccion": "Calle Falsa 123, Córdoba",     "telefono": "351-123-4567", "saldo": 2500.00},
    {"nombre": "María López",   "email": "maria@email.com",  "direccion": "Belgrano 456, Rosario",        "telefono": "341-987-6543", "saldo": 10000.00},
    {"nombre": "Carlos Ruiz",   "email": "carlos@email.com", "direccion": "San Martín 789, Mendoza",      "telefono": "261-456-7890", "saldo": 3200.00},
    {"nombre": "Sofía Torres",  "email": "sofia@email.com",  "direccion": "Mitre 321, Mar del Plata",     "telefono": "223-654-3210", "saldo": 7800.00},
]

clientes = []
for data in clientes_data:
    c, created = Cliente.objects.get_or_create(email=data['email'], defaults=data)
    clientes.append(c)
    if created:
        print(f"  👤 Cliente creado: {c.nombre}")

# Clientes premium
premiums_data = [
    {"cliente": clientes[2], "descuento": 0.15, "puntos": 320, "nivel": "platino"},
    {"cliente": clientes[4], "descuento": 0.10, "puntos": 150, "nivel": "oro"},
    {"cliente": clientes[0], "descuento": 0.05, "puntos": 80,  "nivel": "plata"},
]

for data in premiums_data:
    p, created = ClientePremium.objects.get_or_create(cliente=data['cliente'], defaults={
        "descuento": data['descuento'],
        "puntos":    data['puntos'],
        "nivel":     data['nivel'],
    })
    if created:
        print(f"  ⭐ Premium creado: {p.cliente.nombre} — {p.get_nivel_display()}")

# Compras
compras_data = [
    {"cliente": clientes[0], "producto": "Auriculares Bluetooth",  "precio": 1500.00, "descripcion": "Sony WH-1000XM5"},
    {"cliente": clientes[0], "producto": "Cargador USB-C 65W",     "precio": 800.00,  "descripcion": "Anker PowerPort III"},
    {"cliente": clientes[2], "producto": "Notebook Lenovo IdeaPad","precio": 4250.00, "descripcion": "15.6\" 16GB RAM"},
    {"cliente": clientes[2], "producto": "Mouse Logitech MX Master","precio": 1020.00,"descripcion": "Inalámbrico ergonómico"},
    {"cliente": clientes[4], "producto": "Monitor 27\" QHD",        "precio": 3600.00, "descripcion": "Samsung 165Hz"},
    {"cliente": clientes[1], "producto": "Teclado mecánico",        "precio": 950.00,  "descripcion": "Redragon K530 TKL"},
    {"cliente": clientes[3], "producto": "SSD 1TB NVMe",            "precio": 1100.00, "descripcion": "Samsung 980 Pro"},
]

for data in compras_data:
    c = Compra.objects.create(**data)
    print(f"  🛒 Compra: {c.producto} → {c.cliente.nombre}")

print("\n✅ Base de datos poblada correctamente.")
print("   Accedé al admin en: http://127.0.0.1:8000/admin/")
print("   Usuario: admin | Contraseña: admin1234")
