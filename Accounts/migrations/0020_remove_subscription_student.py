# Generated by Django 3.2 on 2021-06-04 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0019_alter_subscription_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='Student',
        ),
    ]
