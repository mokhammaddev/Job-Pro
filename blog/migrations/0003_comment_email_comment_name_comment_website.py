# Generated by Django 4.2 on 2023-05-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_subcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, max_length=221, null=True),
        ),
    ]
