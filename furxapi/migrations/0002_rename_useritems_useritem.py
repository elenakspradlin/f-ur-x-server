# Generated by Django 4.2.5 on 2023-09-19 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furxapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserItems',
            new_name='UserItem',
        ),
    ]