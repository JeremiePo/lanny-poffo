# Generated by Django 4.2.1 on 2023-08-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_canuserregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='messaging',
            name='mail_to_register',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='messaging',
            name='username_to_register',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
