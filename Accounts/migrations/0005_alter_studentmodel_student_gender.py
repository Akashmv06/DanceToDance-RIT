# Generated by Django 3.2 on 2021-05-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_studentmodel_student_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='student_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=20, verbose_name='Gender'),
        ),
    ]
