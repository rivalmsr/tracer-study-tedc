# Generated by Django 2.2.12 on 2020-06-15 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respons', '0007_responsfempatdetail_respons_header_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsfempatdetail',
            name='master_subkuesioner_id',
        ),
    ]
