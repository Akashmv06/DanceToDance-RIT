# Generated by Django 3.2 on 2021-05-15 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MasterEntry', '0002_rename_complinttype_name_complainttype_complainttype_name'),
        ('Tutor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseVideos',
            new_name='CourseVideo',
        ),
    ]
