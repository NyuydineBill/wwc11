<<<<<<< HEAD
# Generated by Django 4.1.5 on 2023-04-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_prices_monitor_pricess'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllInOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricex', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AllInOne',
                'verbose_name_plural': 'AllInOne',
            },
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricesx', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('dates', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Others',
                'verbose_name_plural': 'Others',
            },
        ),
        migrations.CreateModel(
            name='SmartTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricesss', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'SmartTV',
                'verbose_name_plural': 'SmartTV',
            },
        ),
    ]
=======
# Generated by Django 4.1.5 on 2023-04-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_prices_monitor_pricess'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllInOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricex', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'AllInOne',
                'verbose_name_plural': 'AllInOne',
            },
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricesx', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('dates', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Others',
                'verbose_name_plural': 'Others',
            },
        ),
        migrations.CreateModel(
            name='SmartTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pricesss', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'SmartTV',
                'verbose_name_plural': 'SmartTV',
            },
        ),
    ]
>>>>>>> 5e59e769f249e9ade78b6cfbba69e48ad1ad9dd1
