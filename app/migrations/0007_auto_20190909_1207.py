# Generated by Django 2.2 on 2019-09-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190908_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='result',
        ),
        migrations.AddField(
            model_name='record',
            name='classify',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
