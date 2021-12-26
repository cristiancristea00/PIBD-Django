# Create your models here.
from django.db import models


class Judecator(models.Model):
    id_judecator = models.BigAutoField(db_column='ID_JUDECATOR', primary_key=True)
    cnp = models.CharField(db_column='CNP', unique=True, max_length=13)
    nume = models.CharField(db_column='NUME', max_length=50)
    prenume = models.CharField(db_column='PRENUME', max_length=50)
    telefon = models.CharField(db_column='TELEFON', unique=True, max_length=13)
    email = models.CharField(db_column='EMAIL', unique=True, max_length=50)
    specializare = models.CharField(db_column='SPECIALIZARE', max_length=100)
    preluare_mandat = models.DateField(db_column='PRELUARE_MANDAT')
    expirare_mandat = models.DateField(db_column='EXPIRARE_MANDAT')

    class Meta:
        managed = False
        db_table = 'JUDECATORI'
        ordering = ['prenume', 'nume']

    def __str__(self):
        return F"{self.prenume} {self.nume} ({self.cnp}): {self.email} | {self.telefon}"


class Proces(models.Model):
    id_proces = models.BigAutoField(db_column='ID_PROCES', primary_key=True)
    numar = models.CharField(db_column='NUMĂR', unique=True, max_length=15)
    obiect = models.CharField(db_column='OBIECT', max_length=100)
    materie_juridica = models.CharField(db_column='MATERIE_JURIDICĂ', max_length=50)
    stadiu_procesual = models.CharField(db_column='STADIU_PROCESUAL', max_length=15)
    reclamant = models.CharField(db_column='RECLAMANT', max_length=100)
    parat = models.CharField(db_column='PÂRÂT', max_length=100)

    class Meta:
        managed = False
        db_table = 'PROCESE'
        ordering = ['numar']

    def __str__(self):
        return F"{self.numar} ({self.obiect})"


class Programare(models.Model):
    id_programare = models.BigAutoField(db_column='ID_PROGRAMARE', primary_key=True)
    judecator = models.ForeignKey('Judecator', models.CASCADE, db_column='ID_JUDECATOR')
    proces = models.ForeignKey('Proces', models.CASCADE, db_column='ID_PROCES')
    oras = models.CharField(db_column='ORAȘ', max_length=20)
    locatie = models.CharField(db_column='LOCAȚIE', max_length=50)
    sala = models.CharField(db_column='SALA', max_length=10)
    data = models.DateField(db_column='DATĂ')
    ora = models.TimeField(db_column='ORĂ')

    class Meta:
        managed = False
        db_table = 'PROGRAMARI'
        ordering = ['data', 'ora']

    def __str__(self):
        return F"{self.proces.numar} - {self.judecator.prenume} {self.judecator.nume} ({self.judecator.cnp})"
