# Generated by Django 2.1.3 on 2018-11-28 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='server',
        ),
    ]
