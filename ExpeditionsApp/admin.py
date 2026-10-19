from django.contrib import admin
from .models import Expedition

#Register your models here.

class ExpeditionAdmin(admin.ModelAdmin): # it will surcharge admin per default thats why it enherit the admin
    list_display = ('reference', 'ville_depart', 'ville_arrivee', 'statut')
    list_filter=(
        "ville_depart",
        "ville_arrivee",
        "poids_kg",
        "entreprise",
    )
    readonly_fields=(
        "created_at",
        "updated_at",
        "reference",
    )
    search_fields=(
        "reference",
        "ville_depart",
        "ville_arrivee",
        "entreprise_raison_sociale",
    )

admin.site.register(Expedition, ExpeditionAdmin)  #admin.site.register( nom du model , class de personalisation )