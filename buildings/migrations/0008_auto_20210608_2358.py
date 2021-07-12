# Generated by Django 3.1.5 on 2021-06-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0007_auto_20210602_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='total',
            new_name='total_elevator',
        ),
        migrations.AddField(
            model_name='payment',
            name='total_general',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='total_heating',
            field=models.FloatField(null=True),
        ),
    ]
