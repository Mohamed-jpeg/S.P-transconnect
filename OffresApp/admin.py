from django.contrib import admin
from OffresApp.models import Offre
from django.utils.html import format_html
import csv
from django.http import HttpResponse

# Register your models here.
class OffresAdmin(admin.ModelAdmin):
    list_display=('prix','delai_jours','statut','date_proposition')
    list_filter=(
        "prix",
        "delai_jours",
        "statut",
        "expedition",
    )
    readonly_fields=(
        "created_at",
        "updated_at",

    )
    search_fields=(
        "prix",
        "statut",
        'delai_jours',
        'date_proposition',
        'expedition',
        'transporteur',
        'vehicule',
    )
    list_editable=(
        "statut",
        'delai_jours',
        'date_proposition',
        'expedition',
        'transporteur',
        'vehicule',
    )
    ordering = ('-date_proposition',)
    date_hierarchy = 'date_proposition'
    list_per_page = 25
    autocomplete_fields = ('expedition', 'transporteur', 'vehicule')
    readonly_fields = ('date_proposition', 'created_at', 'updated_at')
    
    fieldsets = (
        ("Détails de l'offre", {
            'fields': ('expedition', 'transporteur', 'vehicule')
        }),
        ("Conditions", {
            'fields': ('prix', 'delai_jours')
        }),
        ("Suivi et État", {
            'fields': ('statut', 'statut_colore', 'date_proposition', 'created_at', 'updated_at')
        }),
    )

    def statut_colore(self,obj):
        couleurs = {
            'proposee': '#F0AD4E',
            'acceptee': '#5CB85C',
            'refusee': '#D9534F',
            'retiree': '#777777',
        }
        return format_html(
            '<span style="color: white; background: {}; padding:3px 8px; border-radius: 4px;">{}</span>',
            couleurs.get(obj.statut, '#999'),
            obj.get_statut_display(),
        )

        @admin.action(description="Exporter la sélection en CSV")
    def exporter_offres_csv(self, modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="offres.csv"'
        writer = csv.writer(response)
        writer.writerow(['reference_expedition', 'transporteur', 'prix', 'statut'])
        for offre in queryset.select_related('expedition', 'transporteur'):
            writer.writerow([
                offre.expedition.reference if offre.expedition else '', 
                offre.transporteur.raison_sociale if offre.transporteur else '', 
                offre.prix, 
                offre.statut
            ])
        return response

admin.site.register(Offre , OffresAdmin)
