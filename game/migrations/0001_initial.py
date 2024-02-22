# Generated by Django 4.2.1 on 2023-07-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedWrestler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrestler_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('promotion', models.CharField(max_length=255)),
                ('active_roles', models.CharField(max_length=255)),
                ('birth_place', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('Weight', models.IntegerField()),
                ('background_in_sports', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('alter_egos', models.CharField(max_length=255)),
                ('roles', models.CharField(max_length=255)),
                ('year_of_beginning', models.CharField(max_length=255)),
                ('in_ring_experience', models.CharField(max_length=255)),
                ('wrestling_style', models.CharField(max_length=255)),
                ('trainer', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('signature_moves', models.CharField(max_length=500)),
                ('career_data', models.TextField(null=True)),
                ('tournament_data', models.TextField(null=True)),
            ],
        ),
    ]
