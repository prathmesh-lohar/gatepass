# Generated by Django 4.2.16 on 2024-10-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_gatepass'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatepass',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
    ]
