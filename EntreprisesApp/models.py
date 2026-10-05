from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator ,RegexValidator,ValidationError


def vallidatee(value):
    if not value:
        raise ValidationError("L'adresse mail est obligatoire.")
    if not value.endswith('@gmail.com'):
        raise ValidationError("L'adresse mail doit se terminer par '@gmail.com'.")

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


matricule_fiscale_validators = RegexValidator(
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="Format invalide. format attendu : 7 chiffres, 1 lettres ( clé de controle), "
     "1 lettre (A/B/D/N/P), 1 lettre (M/P/C/N/E), 3 chiffres""(ex. 1234567AAM000 ou 1234567-A-A-M-000). Exemples : 1234567AAM000, 1234567/A/A/M/000 ou 1234567-A-A-M-000."
)

class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200, null=False)
    matricule_fiscale = models.CharField(
        max_length=17,
        null=False,
        unique=True,
        blank=False,
        validators=[matricule_fiscale_validators]
    )

    adresse = models.TextField(validators=[MinLengthValidator(20,"ladresse doit etre superieur a 20 charactere")])
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