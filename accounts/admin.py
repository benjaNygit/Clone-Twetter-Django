from django.contrib import admin
from .models import Account
from .forms import FormAccountsAdmin

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    form = FormAccountsAdmin
