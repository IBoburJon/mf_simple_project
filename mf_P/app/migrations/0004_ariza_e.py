# Generated by Django 3.2.9 on 2022-02-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220110_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ariza_E',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinfl', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('fname', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('student', models.BooleanField(default=False)),
                ('place', models.CharField(max_length=250)),
            ],
        ),
    ]
