from turtle import title
from typing import override

from django.contrib import messages
from django.utils.html import format_html
from django.contrib import admin
from .models import Expedition
from django.utils import timezone
from OffresApp.models import Offre

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



class OffreInline(admin.TabularInline):
    model = Offre
    extra = 0
    readonly_fields = ('transporteur', 'vehicule', 'prix', 'delai_jours', 'statut', 'date_proposition', 'created_at', 'updated_at')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False



@admin.register(Expedition)
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
    list_editable=(
            'ville_depart',
            'ville_arrivee',
            'description',
            'statut'
    )
    ordering = ('-created_at',)
    date_hierarchy = 'date_souhaitee'
    list_per_page = 25
    inlines = [OffreInline]
    actions = ['cloturer_expeditions']


    @admin.action(description="Clôturer les expéditions sélectionnées")
    def cloturer_expeditions(self, request, queryset):
        count = 0
        for expedition in queryset:
            # Traiter uniquement les expéditions avec le statut en_cours
            if expedition.statut == 'en_cours':
                expedition.statut = 'terminee'
                try:
                    expedition.full_clean()
                    expedition.save()
                    count += 1
                except Exception:
                    pass
        
        self.message_user(
            request,
            f"{count} expédition(s) ont été clôturée(s) avec succès.",
            level=messages.SUCCESS
        )


    @admin.display(description="statut")
    def statut_color(self,obj):
        colors={
            'publie': '#F0AD4E',
            'en_cours': '#0275D8',
            'attribuee': '#5BC0DE',
            'livree': '#5CB85C',
            'annulee': '#D9534F',
        }
        return format_html(
            '<span style="color: white; background: {}; padding:3px 8px; border-radius: 4px;">{}</span>',
            colors.get(obj.statut, '#999'),
            obj.get_statut_display(),
        )
    
    




admin.site.register(Expedition, ExpeditionAdmin)  #admin.site.register( nom du model , class de personalisation )