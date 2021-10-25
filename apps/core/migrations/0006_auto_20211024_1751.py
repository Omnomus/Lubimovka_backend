# Generated by Django 3.2.7 on 2021-10-24 17:51

from django.core.management import call_command
from django.db import migrations


def loadfixture(apps, schema_editor):
    call_command('loaddata', 'settings.json')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211025_1445'),
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]
