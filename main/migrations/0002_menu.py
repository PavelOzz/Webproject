# Generated by Django 4.0.4 on 2022-05-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('massa', models.CharField(max_length=15, verbose_name='Масса')),
                ('price', models.CharField(max_length=15, verbose_name='Цена')),
                ('picture', models.ImageField(upload_to='img/menu/')),
            ],
        ),
    ]
