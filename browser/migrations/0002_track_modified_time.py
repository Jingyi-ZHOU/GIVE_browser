# Generated by Django 3.1 on 2020-08-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='modified_time',
            field=models.TimeField(auto_now=True),
        ),
    ]