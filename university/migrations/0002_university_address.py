# Generated by Django 3.2.18 on 2023-03-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
