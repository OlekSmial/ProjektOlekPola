# Generated by Django 5.1.2 on 2025-01-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='rasa_psa',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
