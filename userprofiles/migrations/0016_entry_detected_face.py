# Generated by Django 5.1.3 on 2024-11-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0015_alter_entry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='detected_face',
            field=models.ImageField(blank=True, null=True, upload_to='detected_faces'),
        ),
    ]