# Generated by Django 5.1.3 on 2024-12-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0017_alter_entry_matching_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='dtected_face_file_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
