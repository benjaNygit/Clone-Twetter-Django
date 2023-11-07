from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.

# Para que se pueda iniciar sesión en el panel de administración
user = get_user_model()
class CustomAdmin(UserAdmin):
    pass

admin.site.register(user, CustomAdmin)
