from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.db.utils import OperationalError, ProgrammingError
from django.core.validators import MinLengthValidator ,RegexValidator,ValidationError
import datetime

def vallidatee(value):
    if not value:
        raise ValidationError("L'adresse mail est obligatoire.")
    if not value.endswith('@gmail.com'):
        raise ValidationError("L'adresse mail doit se terminer par '@gmail.com'.")

def generate_user_id():
    """Génère l'identifiant au format AAuserNN (ex: 26user00)"""
    current_year_str = datetime.date.today().strftime("%y")
    prefix = f"{current_year_str}user"
    
    try:
        last_user = Utilisateur.objects.filter(
            user_id__startswith=prefix
        ).order_by('-user_id').first()
    except (OperationalError, ProgrammingError) as error:
        if "no such table" not in str(error).lower():
            raise
        last_user = None
    
    if last_user:
        try:
            last_counter = int(last_user.user_id[len(prefix):])
            next_counter = last_counter + 1
        except ValueError:
            next_counter = 0
    else:
        next_counter = 0
        
    return f"{prefix}{next_counter:02d}"

class Utilisateur(AbstractUser):
    user_id = models.CharField(
        max_length=8, 
        primary_key=True, 
        default=generate_user_id,
        editable=False,
        validators=[RegexValidator(
            regex=r"^\d{2}user\d{2}$",
            message="Format invalide. Format attendu : AAuserNN (2 chiffres pour l'année, 'user', 2 chiffres pour le compteur, ex. 26user00)."
        )]
    )
    email = models.EmailField(
        unique=True,
        validators=[vallidatee],
        )
    telephone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('chargeur', 'Chargeur'),
            ('transporteur', 'Transporteur'),
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
    matricule_fiscal = models.CharField(
        max_length=17,
        null=False,
        unique=True,
        blank=False,
        validators=[matricule_fiscale_validators],
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
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='entreprise'
    )