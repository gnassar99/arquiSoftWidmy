# Generated by Django 4.1.6 on 2023-03-17 22:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('enfermedades', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('tratamientos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pacientes.paciente')),
            ],
        ),
    ]
