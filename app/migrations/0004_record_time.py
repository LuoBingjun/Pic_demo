# Generated by Django 2.2.5 on 2019-09-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
