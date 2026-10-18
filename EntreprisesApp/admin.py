from django.contrib import admin
from .models import Entreprise, Utilisateur

# Register your models here.

class EntrepriseAdmin(admin.ModelAdmin):
    list_display=('raison_sociale','matricule_fiscal','adresse','type_entreprise','gerant')

class UtilisateurAdmin(admin.ModelAdmin):
    list_display=('user_id','email','telephone','role',) 

admin.site.register(Entreprise , EntrepriseAdmin)
admin.site.register(Utilisateur , UtilisateurAdmin )
