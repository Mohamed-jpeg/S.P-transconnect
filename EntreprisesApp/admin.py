from django.contrib import admin
from .models import Entreprise, Utilisateur

# Register your models here.
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=('raison_sociale','matricule_fiscal','adresse','type_entreprise','gerant')
    list_filter=('adresse', 'type_entreprise')
    readonly_fields=(
        'created_at',
        "updated_at",
        "matricule_fiscal",
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




admin.site.register(Entreprise , EntrepriseAdmin)
admin.site.register(Utilisateur , UtilisateurAdmin )
