# Generated by Django 5.1.2 on 2025-01-17 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0003_student_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='DEPARTMENT',
        ),
    ]
