# Generated by Django 5.0.6 on 2024-06-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_formation_leaverequestadmin_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormationAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('duration', models.DurationField()),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
