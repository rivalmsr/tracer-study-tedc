# Generated by Django 2.2.12 on 2020-05-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuesioner', '0008_auto_20200518_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterfsatu',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='masterfsatu',
            name='kode_pt',
            field=models.PositiveIntegerField(default='045016', editable=False),
        ),
    ]
