# Generated by Django 3.0.5 on 2020-08-24 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20200822_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duyuru',
            name='check_tarih',
        ),
    ]
