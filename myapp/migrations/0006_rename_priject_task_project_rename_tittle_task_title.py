# Generated by Django 5.2 on 2025-04-11 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_project_done_task_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='priject',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='tittle',
            new_name='title',
        ),
    ]
