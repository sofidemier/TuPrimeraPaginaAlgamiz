from django import forms
from .models import Cliente, ClientePremium, Compra


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'direccion', 'telefono', 'saldo']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Ana García', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ej: ana@email.com', 'class': 'form-input'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ej: Av. Corrientes 1234, CABA', 'class': 'form-input'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej: 11-2345-6789', 'class': 'form-input'}),
            'saldo': forms.NumberInput(attrs={'placeholder': '0.00', 'class': 'form-input', 'step': '0.01'}),
        }
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
            'direccion': 'Dirección de envío',
            'telefono': 'Teléfono de contacto',
            'saldo': 'Saldo inicial ($)',
        }


class ClientePremiumForm(forms.ModelForm):
    class Meta:
        model = ClientePremium
        fields = ['cliente', 'descuento', 'puntos', 'nivel']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-input'}),
            'descuento': forms.NumberInput(attrs={'placeholder': '0.10', 'class': 'form-input', 'step': '0.01', 'min': '0', 'max': '1'}),
            'puntos': forms.NumberInput(attrs={'placeholder': '0', 'class': 'form-input', 'min': '0'}),
            'nivel': forms.Select(attrs={'class': 'form-input'}),
        }
        labels = {
            'cliente': 'Cliente a promover',
            'descuento': 'Descuento (ej: 0.15 = 15%)',
            'puntos': 'Puntos iniciales',
            'nivel': 'Nivel premium',
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'producto', 'precio', 'descripcion']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-input'}),
            'producto': forms.TextInput(attrs={'placeholder': 'Ej: Auriculares Bluetooth', 'class': 'form-input'}),
            'precio': forms.NumberInput(attrs={'placeholder': '0.00', 'class': 'form-input', 'step': '0.01', 'min': '0'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción opcional...', 'class': 'form-input', 'rows': 3}),
        }
        labels = {
            'cliente': 'Cliente',
            'producto': 'Nombre del producto',
            'precio': 'Precio ($)',
            'descripcion': 'Descripción (opcional)',
        }


class BusquedaClienteForm(forms.Form):
    busqueda = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Buscar por nombre o email...',
            'class': 'form-input search-input',
            'autofocus': True,
        }),
        label='',
    )
