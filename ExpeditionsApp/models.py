from random import choice, choices
from django.db import models
from EntreprisesApp.models import Entreprise

# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=100,unique=True,)
    ville_depart=models.CharField(max_length=100)
    ville_arrivee=models.CharField(max_length=100)
    poids_kg=models.DecimalField(max_digits=8,decimal_places=2)
    date_souhaitee=models.DateField()
    description=models.TextField(blank=True,null=True)
    entreprise=models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='expeditions'
        )
    statut=models.CharField(
        max_length=50,
        choices=[
            ('publie','Publie'),
            ('attribuee','Attribuee'),
            ('en_cours','En_Cours'),
            ('licree','Livree'),
            ('annulee--defaut publiee','Annulee--Defaut Publiee'),
        ],
        default='publie'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Expedition {self.reference} - {self.statut}"