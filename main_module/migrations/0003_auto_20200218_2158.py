# Generated by Django 3.0.3 on 2020-02-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main_module', '0002_auto_20200218_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='main_image',
            field=models.ImageField(upload_to=''),
        ),
    ]