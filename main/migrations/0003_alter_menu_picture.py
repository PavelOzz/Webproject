# Generated by Django 4.0.4 on 2022-05-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(upload_to='img/menupic/'),
        ),
    ]
