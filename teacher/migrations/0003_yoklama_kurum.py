# Generated by Django 3.0.5 on 2020-08-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_öğretmen_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoklama',
            name='kurum',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
