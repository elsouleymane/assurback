# Generated by Django 5.0.6 on 2024-06-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_adresse'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Employe',
        ),
    ]
