# Generated by Django 2.2.4 on 2020-09-23 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0032_user2_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user2',
            old_name='username',
            new_name='USERNAME_FIELD',
        ),
    ]
