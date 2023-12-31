# Generated by Django 4.2.3 on 2023-07-09 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('WOMEN', 'Women'), ('MEN', 'Men'), ('ELECTRONIC', 'Electronic'), ('ACCESSORIE', 'Accessorie')], default='WOMEN', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=datetime.datetime(2023, 7, 9, 18, 47, 16, 376993, tzinfo=datetime.timezone.utc), max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 's'), ('M', 'm'), ('L', 'l'), ('XL', 'xl'), ('2XL', '2xl'), ('3XL', '3xl')], default='S', max_length=50),
        ),
    ]
