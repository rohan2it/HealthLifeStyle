# Generated by Django 3.1.7 on 2022-01-22 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Herbal_Life', '0002_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='items_json',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]
