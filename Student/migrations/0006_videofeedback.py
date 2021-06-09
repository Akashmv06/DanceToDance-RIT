# Generated by Django 3.2 on 2021-06-08 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0006_coursevideo_cv_thumbnail'),
        ('Accounts', '0021_subscription_substudent'),
        ('Student', '0005_favourites_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='videofeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcontent', models.TextField(max_length=300, null=True, verbose_name='Content')),
                ('vfstudent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.studentmodel', verbose_name='Student')),
                ('vfvideo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tutor.coursevideo', verbose_name='Video:')),
            ],
        ),
    ]
