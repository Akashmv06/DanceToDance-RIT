# Generated by Django 3.2 on 2021-05-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0006_auto_20210526_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancecourses',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]