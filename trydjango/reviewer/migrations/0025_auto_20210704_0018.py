# Generated by Django 3.0 on 2021-07-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0024_auto_20210703_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ReviewSubmission',
            field=models.CharField(default='2021-07-04T00:18', max_length=200),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='DateJoined',
            field=models.CharField(default='2021-07-04T00:18', max_length=200),
        ),
    ]