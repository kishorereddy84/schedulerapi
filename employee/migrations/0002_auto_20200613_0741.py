# Generated by Django 2.1.15 on 2020-06-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='k@k.com', max_length=60),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
