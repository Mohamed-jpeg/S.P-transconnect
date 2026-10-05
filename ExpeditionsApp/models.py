from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
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

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'chargeur':
            raise ValidationError({'entreprise':'une expedition ne peut etre que par une entreprise de type chargeur'})
        
    @classmethod
    def _generate_reference(cls):
        annee = timezone.now().strftime('%y')
        dernier = cls.objects.filter(
            reference__startswith=f"EXP_{annee}_"
        ).order_by('-reference').first()

        compteur = int(dernier.reference[-5:]) + 1 if dernier else 1
        
        if compteur > 99999:
            raise ValidationError("Limite de références atteinte.")
        return f"EXP_{annee}_{compteur:05d}"
    
    def save(self,*args,**kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        self.full_clean()
        super().save(*args,**kwargs)


    


