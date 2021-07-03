# Generated by Django 3.0 on 2021-07-03 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '__first__'),
        ('reviewer', '0021_auto_20210701_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='PaperID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Paper'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ReviewSubmission',
            field=models.CharField(default='2021-07-03T16:02', max_length=200),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='DateJoined',
            field=models.CharField(default='2021-07-03T16:02', max_length=200),
        ),
    ]
