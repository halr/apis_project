# Generated by Django 3.0.1 on 2020-01-02 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_things'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Things',
            new_name='Thing',
        ),
    ]
