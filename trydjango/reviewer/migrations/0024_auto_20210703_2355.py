# Generated by Django 3.0 on 2021-07-03 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0023_auto_20210703_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ReviewSubmission',
            field=models.CharField(default='2021-07-03T23:55', max_length=200),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='DateJoined',
            field=models.CharField(default='2021-07-03T23:55', max_length=200),
        ),
    ]