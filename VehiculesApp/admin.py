from django.contrib import admin
from VehiculesApp.models import Vehicule

# Register your models here.
class VehiculeAdmin(admin.ModelAdmin):
    list_display=('immatriculation','capacite_kg','type_vehicule','disponible')
    list_filter=(
        "capacite_kg",
        "type_vehicule",
        "disponible",
    )
    readonly_fields=(
        "created_at",
        "updated_at",
    )
    search_fields=(
        "immatriculation",
        "capacite_kg",
        'entreprise',
        'type_vehicule',
        'disponible',
    )
    list_editable=(
       "capacite_kg",
        'entreprise',
        'type_vehicule',
        'disponible',
    )
    ordering = ('immatriculation',)
    list_per_page = 25

    fieldsets=(
        ("information vehicule",{
            'fields' : ('immatriculation','type_vehicule','capacite_kg')
        }),
        ("Rattachement et Suivi",{
            'fields':('entreprise','created_at','updated_at')
        })
    )
    autocomplete_fields = ('entreprise',)

admin.site.register(Vehicule , VehiculeAdmin)
