# Generated by Django 2.2.12 on 2020-07-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respons', '0033_auto_20200704_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsfenambelasdetail',
            name='respons',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='responsfsembilandetail',
            name='respons',
            field=models.TextField(),
        ),
    ]