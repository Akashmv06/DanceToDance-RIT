# Generated by Django 3.2 on 2021-05-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0002_auto_20210523_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_loc',
            field=models.CharField(max_length=50, null=True, verbose_name='Location'),
        ),
    ]
