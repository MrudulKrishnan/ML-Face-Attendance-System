# Generated by Django 5.1.2 on 2025-01-25 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0004_remove_student_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendance',
            new_name='AttendanceTable',
        ),
    ]
