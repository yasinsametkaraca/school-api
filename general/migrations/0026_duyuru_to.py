# Generated by Django 3.1.1 on 2020-09-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0025_auto_20200918_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='duyuru',
            name='to',
            field=models.CharField(default='genel', max_length=20),
        ),
    ]
