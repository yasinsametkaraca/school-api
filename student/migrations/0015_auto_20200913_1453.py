# Generated by Django 3.1.1 on 2020-09-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_remove_öğrencidprogramı_ders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='öğrencidprogramı',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
