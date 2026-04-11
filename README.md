# ClienteHub — TuPrimeraPagina+Algamiz

Proyecto web desarrollado con **Django** como parte del curso de Python en **Coderhouse**.

Sistema de gestión de clientes con soporte para clientes estándar, clientes premium con niveles de membresía, y registro de compras.

---

## Tecnologías utilizadas

- Python 3.x
- Django 4.x+
- SQLite (base de datos incluida)
- HTML5 + CSS3 (diseño propio, sin frameworks externos)

---

## Estructura del proyecto

```
TuPrimeraPagina+Algamiz/
├── tuprimerapage/          # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tienda/                 # App principal
│   ├── migrations/         # Migraciones de base de datos
│   ├── templates/tienda/   # Templates HTML
│   │   ├── base.html           ← Template padre (herencia)
│   │   ├── home.html
│   │   ├── lista_clientes.html
│   │   ├── detalle_cliente.html
│   │   ├── lista_premium.html
│   │   ├── lista_compras.html
│   │   ├── buscar.html
│   │   ├── form_cliente.html
│   │   ├── form_premium.html
│   │   └── form_compra.html
│   ├── models.py           # 3 modelos: Cliente, ClientePremium, Compra
│   ├── views.py            # Vistas MVT
│   ├── forms.py            # Formularios
│   ├── urls.py             # URLs de la app
│   └── admin.py            # Panel de administración
├── populate_db.py          # Script para cargar datos de prueba
├── manage.py
└── README.md
```

---

## Modelos (models.py)

| Modelo | Descripción |
|---|---|
| `Cliente` | Nombre, email, dirección, teléfono, saldo |
| `ClientePremium` | Extiende Cliente con descuento, puntos y nivel (Plata/Oro/Platino) |
| `Compra` | Producto, precio, fecha y FK a Cliente |

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/sofialgamiz/TuPrimeraPagina-Algamiz.git
cd TuPrimeraPagina-Algamiz
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

pip install django
```

### 3. Aplicar migraciones

```bash
python manage.py migrate
```

### 4. (Opcional) Cargar datos de prueba

```bash
python populate_db.py
```

Esto crea:
- Superusuario: `admin` / `admin1234`
- 5 clientes de prueba
- 3 clientes premium (Plata, Oro, Platino)
- 7 compras registradas

### 5. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000/**

---

## Orden de prueba de funcionalidades

### Opción A — Con datos de prueba (recomendado)

1. Ejecutar `python populate_db.py`
2. Ir a **http://127.0.0.1:8000/** → ver el Panel de Control con estadísticas
3. Ir a **Clientes** → ver tabla con los 5 clientes cargados
4. Hacer clic en cualquier cliente → ver su detalle, nivel premium y compras
5. Ir a **Premium** → ver los 3 clientes con membresía
6. Ir a **Compras** → ver el listado de compras
7. Ir a **Buscar** → buscar por nombre (ej: "ana") o email (ej: "lopez")

### Opción B — Desde cero (manual)

1. Ir a **http://127.0.0.1:8000/clientes/nuevo/** → cargar un cliente
2. Ir a **http://127.0.0.1:8000/premium/nuevo/** → promoverlo a Premium
3. Ir a **http://127.0.0.1:8000/compras/nueva/** → registrar una compra
4. Ir a **http://127.0.0.1:8000/buscar/** → buscar el cliente creado

### Panel de administración

- URL: **http://127.0.0.1:8000/admin/**
- Usuario: `admin` | Contraseña: `admin1234`

---

## URLs disponibles

| URL | Descripción |
|---|---|
| `/` | Panel de control (home) |
| `/clientes/` | Lista de clientes |
| `/clientes/nuevo/` | Formulario para nuevo cliente |
| `/clientes/<id>/` | Detalle de un cliente |
| `/premium/` | Lista de clientes premium |
| `/premium/nuevo/` | Formulario para nuevo cliente premium |
| `/compras/` | Lista de compras |
| `/compras/nueva/` | Formulario para nueva compra |
| `/buscar/` | Buscador de clientes por nombre o email |
| `/admin/` | Panel de administración de Django |

---

## Requisitos cubiertos

- [x] Herencia de plantillas HTML (`base.html` → todos los templates)
- [x] 3 modelos en `models.py`: `Cliente`, `ClientePremium`, `Compra`
- [x] Formulario de inserción para cada modelo
- [x] Formulario de búsqueda sobre `Cliente` (por nombre y email)
- [x] Patrón MVT de Django

---

## Autora

**Sofía Algamiz** — Coderhouse Python 2025
