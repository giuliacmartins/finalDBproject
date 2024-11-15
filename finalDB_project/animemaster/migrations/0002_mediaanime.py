# Generated by Django 4.1.7 on 2023-03-10 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animemaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediaAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(blank=True, max_length=15)),
                ('episodes', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
