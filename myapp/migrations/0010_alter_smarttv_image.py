# Generated by Django 4.1.5 on 2023-04-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_smarttv_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smarttv',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
