# Generated by Django 2.1.3 on 2018-11-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0005_alert_ipaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='ipAddress',
            field=models.GenericIPAddressField(),
        ),
    ]
