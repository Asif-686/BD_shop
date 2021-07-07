from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.
class Accountadmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'date_joined', 'is_active')
    list_display_links = ('first_name', 'last_name', 'email',
                           'is_active', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, Accountadmin)
