# Generated by Django 5.1.3 on 2024-12-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0023_flagelement_real_t_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_t_match', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='flagelement',
            name='real_t_match',
        ),
    ]
