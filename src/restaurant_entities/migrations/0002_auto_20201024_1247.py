# Generated by Django 3.0 on 2020-10-24 12:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dummysss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique global identifier', unique=True, verbose_name='Global ID')),
                ('test_name', models.CharField(max_length=100)),
                ('test_age', models.PositiveIntegerField()),
                ('test_agss', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dummy',
            name='test_agss',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
