# Generated by Django 5.1.3 on 2024-12-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0020_alter_entry_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlagElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
    ]
