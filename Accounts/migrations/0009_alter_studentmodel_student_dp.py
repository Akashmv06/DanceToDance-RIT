# Generated by Django 3.2 on 2021-05-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_alter_studentmodel_student_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='student_dp',
            field=models.ImageField(upload_to='profile', verbose_name='Profile picture'),
        ),
    ]
