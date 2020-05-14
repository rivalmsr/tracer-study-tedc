from django.db import models


class MasterPoltekTedc(models.Model):
    kode            = models.SmallIntegerField(default='045016')
    nama            = models.CharField(max_length=100)
    status          = models.CharField(max_length=5, default='Aktif')
    email           = models.EmailField(blank=True)
    website         = models.CharField(max_length=100, blank=True)
    alamat          = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


class MasterProdi(models.Model):
    kode            = models.SmallIntegerField()
    nama            = models.CharField(max_length=100)

    STATUS_PRODI = (
        ('A', 'Aktif'),
        ('T', 'Tutup'),
    )
    status          = models.CharField(
                        max_length=5,
                        choices=STATUS_PRODI,
                        default='Tutup',
    )

    LIST_DIPLOMA = (
        ('D1', 'Diploma Satu'),
        ('D3', 'Diploma Tiga'),
        ('D4', 'Diploma Empat'),
    )

    jejang          = models.CharField(
                        max_length=2,
                        choices=LIST_DIPLOMA,
    )
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

