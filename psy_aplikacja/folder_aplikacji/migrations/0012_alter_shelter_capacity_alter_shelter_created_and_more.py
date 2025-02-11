# Generated by Django 5.1.2 on 2025-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0011_alter_money_collection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
