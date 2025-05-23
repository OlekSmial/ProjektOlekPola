# Generated by Django 5.1.2 on 2025-01-20 15:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0003_dog_castrated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='DOG_SIZE',
            new_name='SIZE',
        ),
        migrations.AlterField(
            model_name='dog',
            name='age_type',
            field=models.CharField(choices=[('kitten', 'Kociak'), ('puppy', 'Szczeniak'), ('age', 'Wiek')], default='age', max_length=10),
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('rasa_kota', models.CharField(max_length=60)),
                ('SIZE', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=1)),
                ('month_added', models.IntegerField(choices=[(1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')], default=1)),
                ('age_type', models.CharField(choices=[('kitten', 'Kociak'), ('puppy', 'Szczeniak'), ('age', 'Wiek')], default='age', max_length=10)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('castrated', models.CharField(choices=[('YES', 'TAK'), ('NO', 'NIE')], default='', max_length=10)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='folder_aplikacji.team')),
            ],
        ),
    ]
