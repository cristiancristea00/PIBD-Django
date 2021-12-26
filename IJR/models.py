# Create your models here.
from typing import Final

from django.db import models


class Judecator(models.Model):
    SPECIALIZARE_CHOICES: Final = [
        ('Cauze militare', 'Cauze militare'),
        ('Cauze comerciale', 'Cauze comerciale'),
        ('Cauze de drept constituțional', 'Cauze de drept constituțional'),
        ('Cauze de contencios administrativ și fiscal', 'Cauze de contencios administrativ și fiscal'),
        ('Cauze în materie de dreptul familiei și minori', 'Cauze în materie de dreptul familiei și minori'),
        ('Cauze civile și de executare silită în materie civilă', 'Cauze civile și de executare silită în materie civilă'),
        ('Cauze în materie de conflicte de muncă și asigurări sociale', 'Cauze în materie de conflicte de muncă și asigurări sociale'),
        ('Cauze penale și de punere în executare a hotărârilor pronunțate în materie penală',
         'Cauze penale și de punere în executare a hotărârilor pronunțate în materie penală')
    ]

    id_judecator = models.BigAutoField('ID Judecător', db_column='ID_JUDECATOR', primary_key=True)
    cnp = models.CharField('Cod Numeric Personal (CNP)', db_column='CNP', unique=True, max_length=13)
    nume = models.CharField('Nume', db_column='NUME', max_length=50)
    prenume = models.CharField('Prenume', db_column='PRENUME', max_length=50)
    telefon = models.CharField('Telefon', db_column='TELEFON', unique=True, max_length=13)
    email = models.CharField('Email', db_column='EMAIL', unique=True, max_length=50)
    specializare = models.CharField('Specializare', db_column='SPECIALIZARE', max_length=100, choices=SPECIALIZARE_CHOICES)
    preluare_mandat = models.DateField('Preluare mandat', db_column='PRELUARE_MANDAT')
    expirare_mandat = models.DateField('Expirare mandat', db_column='EXPIRARE_MANDAT')

    class Meta:
        managed = False
        db_table = 'JUDECATORI'
        verbose_name = 'Judecător'
        verbose_name_plural = 'Judecători'
        ordering = ['prenume', 'nume']

    def __str__(self):
        return self.represent

    @property
    def nume_complet(self):
        return F"{self.prenume} {self.nume}"

    @property
    def represent(self):
        return F"{self.nume_complet} ({self.cnp})"


class Proces(models.Model):
    PROCES_CHOICES: Final = [
        ("Apel", "Apel"),
        ("Fond", "Fond"),
        ("Recurs", "Recurs"),
        ("Revizuire", "Revizuire"),
        ("Contestație", "Contestație")
    ]

    id_proces = models.BigAutoField('ID Proces', db_column='ID_PROCES', primary_key=True)
    numar = models.CharField('Număr', db_column='NUMĂR', unique=True, max_length=15)
    obiect = models.CharField('Obiect', db_column='OBIECT', max_length=100)
    materie_juridica = models.CharField('Materie juridică', db_column='MATERIE_JURIDICĂ', max_length=50)
    stadiu_procesual = models.CharField('Stadiu procesual', db_column='STADIU_PROCESUAL', max_length=15, choices=PROCES_CHOICES)
    reclamant = models.CharField('Reclamant', db_column='RECLAMANT', max_length=100)
    parat = models.CharField('Pârât', db_column='PÂRÂT', max_length=100)

    class Meta:
        managed = False
        db_table = 'PROCESE'
        verbose_name = 'Proces'
        verbose_name_plural = 'Procese'
        ordering = ['numar']

    def __str__(self):
        return self.represent

    @property
    def represent(self):
        return F"{self.numar} ({self.obiect})"


class Programare(models.Model):
    id_programare = models.BigAutoField('ID Programare', db_column='ID_PROGRAMARE', primary_key=True)
    judecator = models.ForeignKey(Judecator, models.CASCADE, db_column='ID_JUDECATOR')
    proces = models.ForeignKey(Proces, models.CASCADE, db_column='ID_PROCES')
    oras = models.CharField('Oraș', db_column='ORAȘ', max_length=20)
    locatie = models.CharField('Locație', db_column='LOCAȚIE', max_length=50)
    sala = models.CharField('Sala', db_column='SALA', max_length=10)
    data = models.DateField('Data', db_column='DATĂ')
    ora = models.TimeField('Ora', db_column='ORĂ')

    class Meta:
        managed = False
        db_table = 'PROGRAMARI'
        verbose_name = 'Programare'
        verbose_name_plural = 'Programări'
        ordering = ['data', 'ora']

    def __str__(self):
        return self.represent

    @property
    def represent(self):
        return F"{self.proces.numar} - {self.judecator.prenume} {self.judecator.nume} ({self.judecator.cnp})"
