# Generated by Django 3.0.5 on 2020-05-21 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200520_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='text',
        ),
    ]
