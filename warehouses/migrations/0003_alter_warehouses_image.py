# Generated by Django 3.2.7 on 2021-11-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0002_alter_warehouses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouses',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
