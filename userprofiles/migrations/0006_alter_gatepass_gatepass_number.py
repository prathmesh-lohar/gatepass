# Generated by Django 5.1.1 on 2024-10-24 08:36

import userprofiles.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0005_alter_gatepass_gatepass_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepass',
            name='gatepass_number',
            field=userprofiles.models.GatepassNumberField(blank=True, max_length=10, unique=True),
        ),
    ]