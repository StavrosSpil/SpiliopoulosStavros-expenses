# Generated by Django 3.1.5 on 2021-05-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_auto_20210528_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='document',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
