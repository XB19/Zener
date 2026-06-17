from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DemandeZenCard

@admin.register(DemandeZenCard)
class DemandeZenCardAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'telephone',
        'email',
        'station_retrait',
        'type_demande',
        'date_creation'
    )

    search_fields = (
        'nom',
        'telephone',
        'email'
    )