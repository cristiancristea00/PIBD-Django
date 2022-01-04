from django.db import models, transaction

from IJR.models import Judecator, Proces


class Programare(models.Model):
    id_programare = models.BigAutoField('ID Programare', db_column='ID_PROGRAMARE', primary_key=True)
    judecator = models.ForeignKey(Judecator, on_delete=models.CASCADE, db_column='ID_JUDECATOR')
    proces = models.ForeignKey(Proces, on_delete=models.CASCADE, db_column='ID_PROCES')
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

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()
