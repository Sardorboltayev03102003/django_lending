# Generated by Django 4.2.5 on 2023-09-28 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0002_remove_customer_number_customer_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sardor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255, verbose_name='Ismi')),
                ('description', models.TextField(verbose_name="Ma'lumot")),
            ],
        ),
    ]
