from turtle import title
from typing import override

from django.contrib import admin
from .models import Expedition
from django.utils import timezone

#Register your models here.
class EnRetarFilter(admin.SimpleListFilter):
    title: str='en_retar'
    parameter_name='en_retar'
    def lookups(self, request,model_admin):
        return [('oui','Oui'),('non','Non')]

    @override
    def queryset(self, request, queryset):
        aujourd_hui = timezone.now().date()
        if self.value()== 'oui':
            return queryset.filter(statut='publie',date_souhaitee__lt=aujourd_hui)
        if self.value() == "non":
            return queryset.exclude(statut="publie", date_souhaitee__lt=timezone.now().date())
        return queryset





class ExpeditionAdmin(admin.ModelAdmin): # it will surcharge admin per default thats why it enherit the admin
    list_display = ('reference', 'ville_depart', 'ville_arrivee', 'statut')
    list_filter=(
        "ville_depart",
        "ville_arrivee",
        "poids_kg",
        "entreprise",
        EnRetarFilter,
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
    fieldsets=(
        (
            "Expedition",
            {"fields":("reference","entreprise","description")}
        ),
        (
            "Iteraire et Produit",
            {"fields":("ville_depart","ville_arrivee","poids_kg","date_souhaitee")}
        ),
        (
            "Statut et Horaire",
            {
                "fields":("statut","created_at","updated_at"),
                "classes":("collapse"),
            }
        )
    )



admin.site.register(Expedition, ExpeditionAdmin)  #admin.site.register( nom du model , class de personalisation )