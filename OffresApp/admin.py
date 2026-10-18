from django.contrib import admin
from OffresApp.models import Offre

# Register your models here.
class OffresAdmin(admin.ModelAdmin):
    list_display=('prix','delai_jours','statut','date_proposition')

admin.site.register(Offre , OffresAdmin)
