from pickle import EMPTY_DICT

from django.contrib import admin
from .models import Entreprise, Utilisateur 
from VehiculesApp.models import Vehicule
admin.site.site_header="TransConnect-Administration"
admin.site.site_title="TransConnect-Administration"


class VehiculeInline(admin.TabularInline):
    model = Vehicule
    extra = 0
    # Permet d'afficher et de modifier les véhicules directement depuis la fiche entreprise
    fields = (
        'immatriculation',
         'type_vehicule',
          'capacite_kg',
           'disponible'
           )
    def has_add_permission(self, request, obj=None):
        return True  # Permet d'ajouter des véhicules depuis la fiche entreprise
    
    

# Register your models here.
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=('raison_sociale','matricule_fiscal','adresse','type_entreprise','gerant')
    list_filter=('adresse', 'type_entreprise')
    readonly_fields=(
        'created_at',
        "updated_at",
        "matricule_fiscal",
    )
    fieldsets = (
        ("Entreprise", {"fields": ("raison_sociale", "type_entreprise", "matricule_fiscal", "adresse")}),
        (
            "Gérant",
            {"fields": ("gerant",)},
        ),
        (
            "Horodatage",
            {"fields": ("created_at", "updated_at"),"classes": ("collapse",),},
        ),
    )

    search_fields=(
        'raison_sociale',
        'matricule_fiscal',
        'adresse',
        'type_entreprise',
        'gerant'
    )

    list_editable=(
        'adresse',
        'type_entreprise',
        'gerant',
    )

    ordering = ('raison_sociale',)
    list_per_page = 25
    
    inlines = [VehiculeInline]

    


class UtilisateurAdmin(admin.ModelAdmin):
    list_display=('user_id','email','telephone','role',) 
    
    list_filter=('role',"is_active")
    
    readonly_fields=(
        "user_id",
        "date_joined",
        "last_login",
        "created_at",
        "updated_at",
    )
    fieldsets = (
        ("Utilisateur", {"fields": ("username", "first_name", "last_name", "email", "role", "telephone")}),
        (
            "Horodatage",
            {"fields": ("user_id", "date_joined", "last_login", "created_at", "updated_at"),"classes": ("collapse",),},
        ),
    )
    search_fields=(
        'user_id',
        'email',
        'telephone',
        'role',
    )
    ordering = ('username',)
    list_per_page = 25
    list_editable=(
        'email',
        'telephone',
        'role',
    )
    



admin.site.register(Entreprise , EntrepriseAdmin)
admin.site.register(Utilisateur , UtilisateurAdmin )
