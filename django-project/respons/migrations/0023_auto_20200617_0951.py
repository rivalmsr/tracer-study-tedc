# Generated by Django 2.2.12 on 2020-06-17 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('respons', '0022_auto_20200617_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsfdelapandetail',
            name='respons_header_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='respons.ResponsHeader'),
        ),
        migrations.AddField(
            model_name='responsfsembilandetail',
            name='respons_header_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='respons.ResponsHeader'),
        ),
        migrations.AddField(
            model_name='responsfsepuluhdetail',
            name='respons_header_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='respons.ResponsHeader'),
        ),
    ]