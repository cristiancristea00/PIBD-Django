# Generated by Django 4.0 on 2021-12-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judecator',
            fields=[
                ('id_judecator', models.BigAutoField(db_column='ID_JUDECATOR', primary_key=True, serialize=False, verbose_name='ID Judecător')),
                ('cnp', models.CharField(db_column='CNP', max_length=13, unique=True, verbose_name='Cod Numeric Personal (CNP)')),
                ('nume', models.CharField(db_column='NUME', max_length=50, verbose_name='Nume')),
                ('prenume', models.CharField(db_column='PRENUME', max_length=50, verbose_name='Prenume')),
                ('telefon', models.CharField(db_column='TELEFON', max_length=13, unique=True, verbose_name='Telefon')),
                ('email', models.CharField(db_column='EMAIL', max_length=50, unique=True, verbose_name='Email')),
                ('specializare', models.CharField(choices=[('Cauze militare', 'Cauze militare'), ('Cauze comerciale', 'Cauze comerciale'),
                                                           ('Cauze de drept constituțional', 'Cauze de drept constituțional'), (
                                                               'Cauze de contencios administrativ și fiscal',
                                                               'Cauze de contencios administrativ și fiscal'), (
                                                               'Cauze în materie de dreptul familiei și minori',
                                                               'Cauze în materie de dreptul familiei și minori'), (
                                                               'Cauze civile și de executare silită în materie civilă',
                                                               'Cauze civile și de executare silită în materie civilă'), (
                                                               'Cauze în materie de conflicte de muncă și asigurări sociale',
                                                               'Cauze în materie de conflicte de muncă și asigurări sociale'), (
                                                               'Cauze penale și de punere în executare a hotărârilor pronunțate în materie penală',
                                                               'Cauze penale și de punere în executare a hotărârilor pronunțate în materie penală')],
                                                  db_column='SPECIALIZARE', max_length=100, verbose_name='Specializare')),
                ('preluare_mandat', models.DateField(db_column='PRELUARE_MANDAT', verbose_name='Preluare mandat')),
                ('expirare_mandat', models.DateField(db_column='EXPIRARE_MANDAT', verbose_name='Expirare mandat')),
            ],
            options={
                'verbose_name': 'Judecător',
                'verbose_name_plural': 'Judecători',
                'db_table': 'JUDECATORI',
                'ordering': ['prenume', 'nume'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proces',
            fields=[
                ('id_proces', models.BigAutoField(db_column='ID_PROCES', primary_key=True, serialize=False, verbose_name='ID Proces')),
                ('numar', models.CharField(db_column='NUMĂR', max_length=15, unique=True, verbose_name='Număr')),
                ('obiect', models.CharField(db_column='OBIECT', max_length=100, verbose_name='Obiect')),
                ('materie_juridica', models.CharField(db_column='MATERIE_JURIDICĂ', max_length=50, verbose_name='Materie juridică')),
                ('stadiu_procesual', models.CharField(
                    choices=[('Apel', 'Apel'), ('Fond', 'Fond'), ('Recurs', 'Recurs'), ('Revizuire', 'Revizuire'), ('Contestație', 'Contestație')],
                    db_column='STADIU_PROCESUAL', max_length=15, verbose_name='Stadiu procesual')),
                ('reclamant', models.CharField(db_column='RECLAMANT', max_length=100, verbose_name='Reclamant')),
                ('parat', models.CharField(db_column='PÂRÂT', max_length=100, verbose_name='Pârât')),
            ],
            options={
                'verbose_name': 'Proces',
                'verbose_name_plural': 'Procese',
                'db_table': 'PROCESE',
                'ordering': ['numar'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Programare',
            fields=[
                ('id_programare', models.BigAutoField(db_column='ID_PROGRAMARE', primary_key=True, serialize=False, verbose_name='ID Programare')),
                ('oras', models.CharField(db_column='ORAȘ', max_length=20, verbose_name='Oraș')),
                ('locatie', models.CharField(db_column='LOCAȚIE', max_length=50, verbose_name='Locație')),
                ('sala', models.CharField(db_column='SALA', max_length=10, verbose_name='Sala')),
                ('data', models.DateField(db_column='DATĂ', verbose_name='Data')),
                ('ora', models.TimeField(db_column='ORĂ', verbose_name='Ora')),
            ],
            options={
                'verbose_name': 'Programare',
                'verbose_name_plural': 'Programări',
                'db_table': 'PROGRAMARI',
                'ordering': ['data', 'ora'],
                'managed': False,
            },
        ),
    ]
