# Generated by Django 2.1.15 on 2020-09-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20200912_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hourlyrate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]