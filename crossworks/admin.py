from django.contrib import admin
from .models import formapp


@admin.register(formapp)
class UserEntryAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'ph_no', )
    search_fields=('name',)