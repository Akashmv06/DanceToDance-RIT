# Generated by Django 3.2 on 2021-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0011_feedback_feedstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourites',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
    ]
