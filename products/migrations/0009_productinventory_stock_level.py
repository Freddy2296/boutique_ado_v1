# Generated by Django 3.2.9 on 2022-03-20 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220320_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinventory',
            name='stock_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
