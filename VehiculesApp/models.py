from django.db.models.fields import CharField
from django.db import models
from EntreprisesApp.models import Entreprise

# Create your models here.
class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=20,unique=True)
    capacite_kg=models.PositiveIntegerField()
    entreprise=models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='vehicules',
        )
    type_vehicule=models.CharField(
        max_length=50,
        choices=[
                    ('camionnette', 'Camionnette'),
                    ('fourgon', 'Fourgon'),
                    ('camion_porteur', 'Camion Porteur'),
                    ('semi_remorque', 'Semi-remorque'),
                ],
    )
    disponible=models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.immatriculation} ({self.type_vehicule})"