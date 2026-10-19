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
        "reference",
        "poids_kg",
    )


admin.site.register(Vehicule , VehiculeAdmin)
