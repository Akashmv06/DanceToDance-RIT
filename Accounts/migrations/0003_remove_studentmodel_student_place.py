# Generated by Django 3.2 on 2021-05-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_studentmodel_student_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='student_place',
        ),
    ]
