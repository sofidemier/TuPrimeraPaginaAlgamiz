from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Cliente, ClientePremium, Compra
from .forms import ClienteForm, ClientePremiumForm, CompraForm, BusquedaClienteForm


def home(request):
    """Página de inicio con estadísticas generales."""
    total_clientes = Cliente.objects.count()
    total_premium = ClientePremium.objects.count()
    total_compras = Compra.objects.count()
    ultimas_compras = Compra.objects.select_related('cliente').all()[:5]
    context = {
        'total_clientes': total_clientes,
        'total_premium': total_premium,
        'total_compras': total_compras,
        'ultimas_compras': ultimas_compras,
    }
    return render(request, 'tienda/home.html', context)


# ─── CLIENTES ────────────────────────────────────────────────────────────────

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tienda/lista_clientes.html', {'clientes': clientes})


def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'✅ Cliente "{cliente.nombre}" creado correctamente.')
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'tienda/form_cliente.html', {'form': form, 'titulo': 'Nuevo Cliente'})


def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    compras = cliente.compra_set.all()
    es_premium = hasattr(cliente, 'premium')
    context = {
        'cliente': cliente,
        'compras': compras,
        'es_premium': es_premium,
    }
    return render(request, 'tienda/detalle_cliente.html', context)


# ─── CLIENTES PREMIUM ────────────────────────────────────────────────────────

def lista_premium(request):
    premiums = ClientePremium.objects.select_related('cliente').all()
    return render(request, 'tienda/lista_premium.html', {'premiums': premiums})


def nuevo_premium(request):
    # Solo clientes que aún no son premium
    clientes_sin_premium = Cliente.objects.filter(premium__isnull=True)
    if not clientes_sin_premium.exists():
        messages.warning(request, '⚠️ Todos los clientes ya son premium. Creá un cliente nuevo primero.')
        return redirect('lista_premium')

    if request.method == 'POST':
        form = ClientePremiumForm(request.POST)
        if form.is_valid():
            premium = form.save()
            messages.success(request, f'⭐ "{premium.cliente.nombre}" ahora es Cliente Premium {premium.get_nivel_display()}.')
            return redirect('lista_premium')
    else:
        form = ClientePremiumForm()
        form.fields['cliente'].queryset = clientes_sin_premium

    return render(request, 'tienda/form_premium.html', {'form': form, 'titulo': 'Nuevo Cliente Premium'})


# ─── COMPRAS ─────────────────────────────────────────────────────────────────

def lista_compras(request):
    compras = Compra.objects.select_related('cliente').all()
    return render(request, 'tienda/lista_compras.html', {'compras': compras})


def nueva_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            messages.success(request, f'🛒 Compra de "{compra.producto}" registrada para {compra.cliente.nombre}.')
            return redirect('lista_compras')
    else:
        form = CompraForm()
    return render(request, 'tienda/form_compra.html', {'form': form, 'titulo': 'Nueva Compra'})


# ─── BÚSQUEDA ────────────────────────────────────────────────────────────────

def buscar_cliente(request):
    form = BusquedaClienteForm(request.GET or None)
    resultados = None
    query = ''

    if form.is_valid():
        query = form.cleaned_data.get('busqueda', '')
        if query:
            resultados = Cliente.objects.filter(
                Q(nombre__icontains=query) | Q(email__icontains=query)
            )
        else:
            resultados = Cliente.objects.all()

    return render(request, 'tienda/buscar.html', {
        'form': form,
        'resultados': resultados,
        'query': query,
    })
