# Generated by Django 2.2.3 on 2020-07-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respons', '0029_remove_responsfempatdetail_master_subkuesioner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsfempatdetail',
            name='respons',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='responsfenambelasdetail',
            name='respons',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='responsfsembilandetail',
            name='respons',
            field=models.CharField(max_length=255),
        ),
    ]
