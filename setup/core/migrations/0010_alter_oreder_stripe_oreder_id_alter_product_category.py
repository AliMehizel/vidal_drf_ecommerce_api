# Generated by Django 4.2.3 on 2023-08-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_oreder_id_oreder_stripe_oreder_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oreder',
            name='stripe_oreder_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('WOMEN', 'WOMEN'), ('MEN', 'MEN'), ('JEWELERY', 'JEWELERY'), ('KIDS', 'KIDS')], default='WOMEN', max_length=50),
        ),
    ]
