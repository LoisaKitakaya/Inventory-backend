# Generated by Django 4.0.3 on 2022-03-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='quantity',
            new_name='quantity_mass_volume',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='measurement_in',
            field=models.CharField(choices=[('L', 'Liters'), ('ml', 'Milliliters'), ('Kg', 'Kilograms'), ('g', 'Grams'), ('P_', 'Pairs'), ('s', 'Single object(s)')], default='s', max_length=50),
        ),
    ]
