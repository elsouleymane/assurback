# Generated by Django 5.0.6 on 2024-06-18 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_adminactiondemande'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
