# Generated by Django 4.2.6 on 2023-11-30 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_bookingreq_rstatus_bookingreq_tcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingreq',
            name='tcost',
            field=models.IntegerField(default=500, validators=[django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
