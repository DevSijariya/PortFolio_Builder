# Generated by Django 4.2.9 on 2024-02-29 15:44

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.user_directory_path),
        ),
    ]
