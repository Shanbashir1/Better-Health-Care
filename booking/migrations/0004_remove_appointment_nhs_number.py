# Generated by Django 3.2.16 on 2023-01-06 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20230106_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='nhs_number',
        ),
    ]
