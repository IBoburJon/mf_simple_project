# Generated by Django 3.2.9 on 2022-01-10 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='token_created',
        ),
    ]