# Generated by Django 3.2.6 on 2021-11-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer_WH_Owner_Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.CharField(max_length=20)),
                ('wh_owner_id', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('wh_store_number', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]