# Generated by Django 3.0.8 on 2020-08-05 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_coordinates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinates',
            old_name='track_id',
            new_name='track',
        ),
    ]
