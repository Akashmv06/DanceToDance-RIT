# Generated by Django 3.2 on 2021-05-23 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_date',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_loc',
        ),
    ]
