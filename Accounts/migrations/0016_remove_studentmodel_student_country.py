# Generated by Django 3.2 on 2021-05-25 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0015_auto_20210525_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='student_country',
        ),
    ]