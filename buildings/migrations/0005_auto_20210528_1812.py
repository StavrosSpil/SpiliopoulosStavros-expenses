# Generated by Django 3.1.5 on 2021-05-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_auto_20210528_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='month',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
