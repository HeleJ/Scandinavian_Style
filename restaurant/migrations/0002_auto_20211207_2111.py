# Generated by Django 3.2.9 on 2021-12-07 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meals',
            new_name='restaurant',
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={},
        ),
    ]
