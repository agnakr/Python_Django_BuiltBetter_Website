# Generated by Django 4.2 on 2023-07-08 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0002_contact_delete_contact_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
