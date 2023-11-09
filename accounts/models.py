from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

import secrets

# Create your models here.

class Account(AbstractUser):
    """Cuentas de usuario personalizadas
    Quita campos del modelo original ademas de agregar nuevos.
    Campos heredados:
        - password      (varchar(128))
        - last_login    (datetime)
        - is_superuser  (bool)
        - username      (varchar(150))
        - email         (varchar(254)
        - is_staff      (bool)
        - is_active     (bool) -> Necesario para iniciar sesión en panel admin
        - date_joined   (datetime)
    """
    id = models.CharField(primary_key=True, max_length=5, unique=True, editable=False)
    email = models.EmailField(_("email address"), null=False, unique=True) # copiado directamente
    first_name = None
    last_name = None
    name = models.CharField(max_length=50, blank=True)
    birthday_date = models.DateField(null=False)
    biography = models.CharField(max_length=160, blank=True)
    location = models.CharField(max_length=30, blank=True)
    foto_perfil = models.ImageField(upload_to='images/perfil/', blank=True)
    foto_background = models.ImageField(upload_to='images/background/', blank=True)

    USERNAME_FIELD = 'email' # se inicia sesión con email
    REQUIRED_FIELDS = ['birthday_date', 'username']

    def save(self, *args, **kwargs):
        """Guarda automáticamente un token como clave primaria (id)"""
        if not self.id:
            self.id = secrets.token_hex(5)
        super(Account, self).save(*args, **kwargs)

class Following(models.Model):
    """Modelo para guardar los seguidores de cada cuenta
    Se genera una nueva fila por cada vez que un usuario sigue a otro.
    Se debe de borrar la fila si se deja de seguir.
    """
    id = models.CharField(primary_key=True, max_length=20, unique=True, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')
    follow = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='followers')

    def save(self, *args, **kwargs):
        """Guarda automáticamente un token como clave primaria (id)"""
        if not self.id:
            self.id = secrets.token_hex(20)
        super(Following, self).save(*args, **kwargs)
