# Generated by Django 2.1.15 on 2020-08-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200823_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
