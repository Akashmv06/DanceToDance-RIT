# Generated by Django 3.2 on 2021-06-01 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tutor', '0006_coursevideo_cv_thumbnail'),
        ('Accounts', '0017_studentmodel_student_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fdate', models.DateTimeField(auto_now_add=True, verbose_name='Date & Time:')),
                ('fstudent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.studentmodel', verbose_name='Student:')),
                ('fvideo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tutor.coursevideo', verbose_name='Video:')),
            ],
        ),
    ]
