from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

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
    email = models.EmailField(_("email address"), null=False, unique=True) # copiado directamente
    first_name = None
    last_name = None
    name = models.CharField(max_length=50, null=False)
    birthday_date = models.DateField(null=False)
    biography = models.CharField(max_length=160)
    location = models.CharField(max_length=30)
    foto_perfil = models.ImageField(upload_to='images/perfil/', null=True)
    foto_background = models.ImageField(upload_to='images/background/', null=True)

    USERNAME_FIELD = 'email' # se inicia sesión con email
    REQUIRED_FIELDS = ['birthday_date', 'username']
