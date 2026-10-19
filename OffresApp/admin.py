from django.contrib import admin
from OffresApp.models import Offre

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
        "stastus",
    )

admin.site.register(Offre , OffresAdmin)
