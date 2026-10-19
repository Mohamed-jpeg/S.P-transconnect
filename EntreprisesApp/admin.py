from django.contrib import admin
from .models import Entreprise, Utilisateur
admin.site.site_header="TransConnect-Administration"
admin.site.site_title="TransConnect-Administration"

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
    



admin.site.register(Entreprise , EntrepriseAdmin)
admin.site.register(Utilisateur , UtilisateurAdmin )
