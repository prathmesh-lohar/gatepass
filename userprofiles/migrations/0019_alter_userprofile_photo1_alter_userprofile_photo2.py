# Generated by Django 5.1.3 on 2024-12-08 09:12

import userprofiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0018_entry_dtected_face_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to=userprofiles.models.UserProfilePhotoPath(1)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to=userprofiles.models.UserProfilePhotoPath(2)),
        ),
    ]
