# Generated by Django 3.0 on 2020-11-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_entities', '0008_booking_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='table_code',
        ),
        migrations.AddField(
            model_name='table',
            name='code',
            field=models.IntegerField(default=-1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='name',
            field=models.CharField(default='A2', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
