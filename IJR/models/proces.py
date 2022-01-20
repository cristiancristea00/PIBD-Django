from typing import Final

from django.db import models, transaction


class Proces(models.Model):
    PROCES_CHOICES: Final = [
        ('Apel', 'Apel'),
        ('Fond', 'Fond'),
        ('Recurs', 'Recurs'),
        ('Revizuire', 'Revizuire'),
        ('Contestație', 'Contestație')
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
        return F'{self.numar} ({self.obiect})'

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()
