# Generated by Django 2.2.12 on 2020-05-18 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kuesioner', '0006_auto_20200516_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiodataLulusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=12)),
                ('verifikasi_email', models.BooleanField(default=False)),
                ('angkatan', models.SmallIntegerField()),
                ('pekerjaan', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('alamat', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('master_fsatu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kuesioner.MasterFSatu')),
            ],
        ),
    ]