# Generated by Django 5.1.3 on 2024-11-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0011_alter_entry_time_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='gatepass',
        ),
    ]
