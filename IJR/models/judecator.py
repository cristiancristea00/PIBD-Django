from typing import Final

from django.db import models, transaction


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

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()
