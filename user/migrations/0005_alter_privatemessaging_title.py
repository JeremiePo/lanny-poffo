# Generated by Django 4.2.1 on 2023-08-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_privatemessaging'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatemessaging',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
