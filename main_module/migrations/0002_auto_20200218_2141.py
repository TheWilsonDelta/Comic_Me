# Generated by Django 3.0.3 on 2020-02-18 21:41

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='main_image',
            field=models.FileField(upload_to=django.core.files.storage.FileSystemStorage(location='/media')),
        ),
    ]
