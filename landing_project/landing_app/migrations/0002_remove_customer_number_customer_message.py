# Generated by Django 4.2.5 on 2023-09-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='number',
        ),
        migrations.AddField(
            model_name='customer',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
