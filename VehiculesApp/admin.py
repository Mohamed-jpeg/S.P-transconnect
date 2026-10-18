from django.contrib import admin
from VehiculesApp.models import Vehicule

# Register your models here.
class VehiculeAdmin(admin.ModelAdmin):
    list_display=('immatriculation','capacite_kg','type_vehicule','disponible')

admin.site.register(Vehicule , VehiculeAdmin)
