# Generated by Django 5.1.7 on 2025-03-14 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_remove_transport_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='image',
        ),
    ]
