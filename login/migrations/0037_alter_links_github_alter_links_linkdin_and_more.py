# Generated by Django 4.2.9 on 2024-03-26 05:49

import django.core.validators
from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0036_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='github',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='linkdin',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), login.models.validate_photo_size]),
        ),
    ]
