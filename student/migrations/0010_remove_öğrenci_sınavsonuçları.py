# Generated by Django 3.0.5 on 2020-09-07 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20200831_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='öğrenci',
            name='sınavsonuçları',
        ),
    ]
