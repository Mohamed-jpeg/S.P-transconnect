from django import forms
from .models import Vehicule


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields=[
            "immatriculation",
            "capacite_kg",
            'entreprise',
            'type_vehicule',
            'disponible',
        ]
        widgets = {
            'disponible': forms.CheckboxInput(),
        }