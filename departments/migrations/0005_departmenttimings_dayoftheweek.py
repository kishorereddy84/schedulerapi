# Generated by Django 2.1.15 on 2020-07-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_auto_20200724_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmenttimings',
            name='dayOfTheWeek',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
