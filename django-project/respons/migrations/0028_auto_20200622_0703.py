# Generated by Django 2.2.12 on 2020-06-22 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0020_auto_20200606_1416'),
        ('respons', '0027_auto_20200622_0701'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResponsFTujuhBbelasADetail',
            new_name='ResponsFTujuhbelasADetail',
        ),
        migrations.RenameModel(
            old_name='ResponsFTujuhAbelasADetail',
            new_name='ResponsFTujuhbelasBDetail',
        ),
    ]
