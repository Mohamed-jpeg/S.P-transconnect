from django import forms
from .models import Entreprise , Utilisateur


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

class UtulisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields=[
            'username',
            'email',
            'role',
        ]