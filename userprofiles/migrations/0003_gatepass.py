# Generated by Django 4.2.16 on 2024-10-21 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userprofiles.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofiles', '0002_rename_userprofiles_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='gatepass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatepass_number', userprofiles.models.GatepassNumberField(max_length=10, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('date_in', models.DateField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('pass_type', models.CharField(choices=[('guest', 'guest'), ('vip', 'vip')], default='guest', max_length=10)),
                ('master_admin_approval', models.CharField(choices=[('pass', 'pass'), ('pending', 'pending'), ('reject', 'reject')], default='pending', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]