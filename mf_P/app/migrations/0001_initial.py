# Generated by Django 3.2.9 on 2022-01-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=250)),
                ('token_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]