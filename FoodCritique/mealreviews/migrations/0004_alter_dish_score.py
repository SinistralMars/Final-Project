# Generated by Django 4.1.2 on 2022-12-13 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealreviews', '0003_rename_restuarant_dish_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
