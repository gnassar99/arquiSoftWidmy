# Generated by Django 4.1.6 on 2023-04-12 02:13

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('historiasClinicas', '0004_historiaclinica_enfermedades_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='enfermedades',
            field=jsonfield.fields.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='tratamientos',
            field=jsonfield.fields.JSONField(default=list),
        ),
    ]
