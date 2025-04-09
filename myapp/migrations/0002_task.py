# Generated by Django 5.2 on 2025-04-09 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('priject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
