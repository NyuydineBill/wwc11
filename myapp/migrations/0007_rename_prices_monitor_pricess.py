# Generated by Django 4.1.5 on 2023-04-16 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_monitor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitor',
            old_name='prices',
            new_name='pricess',
        ),
    ]
