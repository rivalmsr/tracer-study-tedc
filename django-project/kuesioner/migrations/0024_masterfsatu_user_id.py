# Generated by Django 2.2.12 on 2020-10-04 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuesioner', '0023_auto_20200923_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterfsatu',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
