# Generated by Django 2.2.12 on 2020-07-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lulusan', '0006_auto_20200724_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatalulusan',
            name='pendidikan_terakhir',
            field=models.CharField(blank=True, default='-belum diisi-', max_length=255),
        ),
        migrations.AlterField(
            model_name='biodatalulusan',
            name='akun_linkendin',
            field=models.CharField(blank=True, default='-belum diisi-', max_length=255),
        ),
        migrations.AlterField(
            model_name='biodatalulusan',
            name='alamat',
            field=models.TextField(blank=True, default='-belum diisi-'),
        ),
        migrations.AlterField(
            model_name='biodatalulusan',
            name='angkatan',
            field=models.CharField(blank=True, default='-belum diisi-', max_length=5),
        ),
        migrations.AlterField(
            model_name='biodatalulusan',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('Perempuan', 'Perempuan'), ('Laki-laki', 'Laki-laki')], default='-belum diisi-', max_length=12),
        ),
        migrations.AlterField(
            model_name='biodatalulusan',
            name='pekerjaan',
            field=models.CharField(blank=True, default='-belum diisi-', max_length=100),
        ),
        migrations.AlterField(
            model_name='biodatalulusan',
            name='status',
            field=models.CharField(blank=True, choices=[('Lajang', 'Lajang'), ('Sudah Menikah', 'Sudah Menikah')], default='-belum diisi-', max_length=15),
        ),
    ]
