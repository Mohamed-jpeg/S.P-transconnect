from django import forms
from .models import Entreprise


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = [
            "raison_sociale",
            "matricule_fiscal",
            "adresse",
            "type_entreprise",
            "gerant",
        ]