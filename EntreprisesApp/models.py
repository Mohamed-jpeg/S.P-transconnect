from django.contrib.auth.models import AbstractUser
from django.db import models

class Utulisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('chargeur', 'Chargeur'),
            ('trasporteur', 'Transporteur'),
            ('administration', 'Administration'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200, null=False)
    matricule_fiscale = models.CharField(
        max_length=17,
        null=False,
        unique=True,
        blank=False,
    )
    adresse = models.TextField()
    type_entreprise = models.CharField(
        max_length=100,
        choices=[
            ('chargeur', 'Chargeur'),
            ('transporteur', 'Transporteur'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(
        Utulisateur,
        on_delete=models.CASCADE,
        related_name='entreprise'
    )