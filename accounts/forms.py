from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class FormAccountsAdmin(UserCreationForm):
    """Formulario de registro de Accounts para el panel de administración
    Sobre escribimos el formulario por defecto y le agregamos más campos
    """
    class Meta:
        model = Account
        fields = ('email', 'username', 'birthday_date', 'is_staff')
