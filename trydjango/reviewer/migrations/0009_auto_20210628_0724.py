# Generated by Django 3.0 on 2021-06-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0008_auto_20210628_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ReviewSubmission',
            field=models.CharField(default='2021-06-28T07:24', max_length=200),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='DateJoined',
            field=models.CharField(default='2021-06-28T07:24', max_length=200),
        ),
    ]
