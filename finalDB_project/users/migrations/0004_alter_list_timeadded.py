# Generated by Django 4.1.7 on 2023-03-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='timeadded',
            field=models.TimeField(auto_now_add=True),
        ),
    ]