# Generated by Django 3.0 on 2021-07-14 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0015_auto_20210714_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ReviewSubmission',
        ),
    ]
