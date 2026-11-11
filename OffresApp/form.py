from django import forms
from .models import Offre

class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = [
            'prix',
            'delai_jours',
            'statut',
            'expedition',
            'transporteur',
            'vehicule',
        ]