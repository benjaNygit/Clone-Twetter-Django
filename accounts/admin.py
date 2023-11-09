from django.contrib import admin
from .models import Account, Following
from .forms import FormAccountsAdmin

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    form = FormAccountsAdmin

@admin.register(Following)
class FollowingAdmin(admin.ModelAdmin):
    fields = ('account', 'follow')
