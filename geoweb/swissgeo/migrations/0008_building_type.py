# Generated by Django 3.2.25 on 2024-06-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swissgeo', '0007_building_lift'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='type',
            field=models.CharField(choices=[('restaurant', 'restaurant'), ('liftstation', 'liftstation'), ('shop', 'shop'), ('toilet', 'toilet')], default='restaurant', max_length=100),
        ),
    ]