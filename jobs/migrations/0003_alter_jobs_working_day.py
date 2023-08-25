# Generated by Django 4.2 on 2023-05-05 04:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_categoryjobs_tagjobs_jobs_category_jobs_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='working_day',
            field=models.IntegerField(default=15, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(15)]),
        ),
    ]
