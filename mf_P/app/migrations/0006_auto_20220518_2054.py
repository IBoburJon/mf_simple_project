# Generated by Django 3.2.9 on 2022-05-18 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_ariza_e_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ariza_e',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='pinfl',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='student',
        ),
        migrations.RemoveField(
            model_name='ariza_e',
            name='surname',
        ),
    ]
