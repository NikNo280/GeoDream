# Generated by Django 3.0.5 on 2020-05-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Verified',
            field=models.NullBooleanField(default=False),
        ),
    ]
