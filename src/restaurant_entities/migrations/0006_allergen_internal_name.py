# Generated by Django 3.0 on 2020-11-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_entities', '0005_auto_20201103_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergen',
            name='internal_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
