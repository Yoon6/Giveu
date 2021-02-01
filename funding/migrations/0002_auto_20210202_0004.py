# Generated by Django 3.1.5 on 2021-02-01 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='funding',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/fundings/'),
            preserve_default=False,
        ),
    ]
