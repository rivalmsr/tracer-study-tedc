# Generated by Django 2.2.12 on 2020-07-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respons', '0034_auto_20200704_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsftigadetail',
            name='respons',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]