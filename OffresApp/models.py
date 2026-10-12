from django.core import validators
from django.db import models
from django.db.models.base import ValidationError
from ExpeditionsApp.models import Expedition
from EntreprisesApp.models import Entreprise
from VehiculesApp.models import Vehicule



class Offre(models.Model):

    prix = models.DecimalField(max_digits=10, decimal_places=2,validators=[validators.MinValueValidator(1)])
    delai_jours = models.PositiveIntegerField(validators=[validators.MinValueValidator(1)])
    statut = models.CharField(
        max_length=20,
        choices=[
        ('proposee', 'Proposée'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
        ('retiree', 'Retirée'),
    ],
        default='proposee'
    )
    date_proposition = models.DateField(auto_now_add=True)
    expedition = models.ForeignKey(
        Expedition,
        on_delete=models.CASCADE,
        related_name='offres'
    )
    transporteur = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='offres_proposees'
    )
    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Offre #{self.delai_jours} - {self.prix} TND ({self.statut})"
    
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)

        if self.statut=="acceptee":
            self.expedition.statut="attribuee"
            self.expedition.save()
            self.expedition.offres.exclude(pk=self).filter(statut="proposee").update(statut="refusee")
    
    def clean(self):
        super.clean()

        #1
        if self.transporteur_id and self.transporteur.type_entreprise !="transporteur":
            raise ValidationError("transporteur : Seule une entreprise de type 'transporteur' peut proposer une offre.")
        
        #2
        if self.vehicule_id and self.transporteur_id and self.vehicule.entreprise_id != self.transporteur_id :
                    raise ValidationError("Le véhicule sélectionné n'appartient pas à votre entreprise.")
        
        #3
        if self.expedition_id  and self.expedition_statut != "publiee":
            raise ValidationError("Cette expédition n'est plus ouverte aux offres.")

        #4 honesstly i didnt know how to do it even with ai yit is hard 

        #6
        if self.vehicule_id and not self.pk:#self.pk==primary key 
            if not self.vehicule.disponible:
                raise ValidationError({
                    "vehicule": (
                        "Ce véhicule n'est pas disponible pour de nouvelles offres."
                    )
                })
        
        #7
        if self.vehicule_id and self.expedition_id:
            weight = self.expedition.poids_kg
            vehicule_type = self.vehicule.type_vehicule

            if vehicule_type == "camionnette" and weight > 1500:
                raise ValidationError({
                    "vehicule": (
                        "La camionnette ne supporte pas un poids supérieur à 1,5 tonne"
                        f" ({weight} kg)."
                    )
                })
            elif vehicule_type == "fourgon" and weight > 3500:
                raise ValidationError({
                    "vehicule": (
                        "Le fourgon ne supporte pas un poids supérieur à 3,5 tonnes"
                        f" ({weight} kg)."
                    )
                })
            elif vehicule_type == "camion_porteur" and (weight < 3500 or weight > 19000):
                raise ValidationError({
                    "vehicule": (
                        "Le camion porteur est adapté pour un poids entre 3,5 et 19"
                        f" tonnes (actuel : {weight} kg)."
                    )
                })
            elif vehicule_type == "semi_remorque" and weight < 19000:
                raise ValidationError({
                    "vehicule": (
                        "La semi-remorque est adaptée pour un poids supérieur à 19"
                        f" tonnes (actuel : {weight} kg)."
                    )
                })


        
