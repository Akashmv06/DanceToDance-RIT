# Generated by Django 3.2 on 2021-06-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_remove_favourites_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourites',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]