# Generated by Django 3.0 on 2021-07-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_auto_20210708_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='PaperTitle',
        ),
        migrations.AlterField(
            model_name='review',
            name='ReviewSubmission',
            field=models.CharField(default='2021-07-08T19:22', max_length=200),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='DateJoined',
            field=models.CharField(default='2021-07-08T19:22', max_length=200),
        ),
    ]