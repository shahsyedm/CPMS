# Generated by Django 3.0 on 2021-06-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0010_auto_20210628_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ReviewSubmission',
            field=models.CharField(default='2021-06-28T17:46', max_length=200),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='DateJoined',
            field=models.CharField(default='2021-06-28T17:46', max_length=200),
        ),
    ]
