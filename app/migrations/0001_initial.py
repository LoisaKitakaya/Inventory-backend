# Generated by Django 4.0.3 on 2022-03-17 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('condition', models.CharField(choices=[('EXLNT', 'Excellent'), ('GD', 'Good'), ('AVG', 'Average'), ('BD', 'Bad'), ('PR', 'Poor')], default='AVG', max_length=50)),
                ('type_make_model', models.CharField(max_length=200)),
                ('more_details', models.TextField()),
                ('archived_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item', to='app.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item', to='app.location')),
            ],
            options={
                'ordering': ['-archived_on'],
            },
        ),
    ]
