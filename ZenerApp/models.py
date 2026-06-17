from django.db import models

# Create your models here.
from django.db import models


class ContactMessage(models.Model):

    nom = models.CharField(
        max_length=255
    )

    email = models.EmailField()

    telephone = models.CharField(
        max_length=100,
        blank=True
    )

    sujet = models.CharField(
        max_length=255
    )

    message = models.TextField()

    lu = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
    

    

class JobOffer(models.Model):

    CONTRATS = (
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
        ('Temps plein', 'Temps plein'),
        ('Temps partiel', 'Temps partiel'),
    )

    titre = models.CharField(
        max_length=255
    )

    ville = models.CharField(
        max_length=150
    )

    type_contrat = models.CharField(
        max_length=50,
        choices=CONTRATS
    )

    departement = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField()

    missions = models.TextField()

    profil = models.TextField()

    date_limite = models.DateField(
        null=True,
        blank=True
    )

    actif = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre
    


class JobApplication(models.Model):

    offre = models.ForeignKey(
        JobOffer,
        on_delete=models.CASCADE,
        related_name='candidatures',
        null=True,
        blank=True
    )

    nom = models.CharField(
        max_length=255
    )

    email = models.EmailField()

    telephone = models.CharField(
        max_length=100
    )

    message = models.TextField(
        blank=True
    )

    cv = models.FileField(
        upload_to='candidatures/cv/'
    )

    lettre_motivation = models.FileField(
        upload_to='candidatures/lettres/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nom
    
    
    traitee = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


from django.db import models

class DemandeZenCard(models.Model):

    TYPE_CHOIX = (
        ('Particulier', 'Particulier'),
        ('Entreprise', 'Entreprise'),
    )

    STATIONS_CHOIX = (
        ('Zener Hedzranawoe', 'Zener Hedzranawoe'),
        ('Zener Adidogome', 'Zener Adidogome'),
        ('Zener Agoe', 'Zener Agoe'),
        ('Zener GTA', 'Zener GTA'),
        ('Zener Port', 'Zener Port'),
        ('Zener Baguida', 'Zener Baguida'),
        ('Zener Kpalime', 'Zener Kpalime'),
        ('Zener Atakpame', 'Zener Atakpame'),
        ('Zener Sokode', 'Zener Sokode'),
        ('Zener Kara', 'Zener Kara'),
        ('Zener Dapaong', 'Zener Dapaong'),
    )

    STATUT_CHOICES = (
    ('en_attente', 'En attente'),
    ('validee', 'Validée'),
    ('rejetee', 'Rejetée'),
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )

    nom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    ville = models.CharField(max_length=100)

    type_demande = models.CharField(
        max_length=20,
        choices=TYPE_CHOIX
    )

    station_retrait = models.CharField(
        max_length=100,
        choices=STATIONS_CHOIX
    )

    cni = models.ImageField(
        upload_to='zencard/cni/'
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nom
    


class Actualite(models.Model):

    titre = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualites/')
    created_at = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.titre