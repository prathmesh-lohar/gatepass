# Generated by Django 5.1.3 on 2024-12-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0021_flagelement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flagelement',
            name='flag',
            field=models.IntegerField(default=0),
        ),
    ]