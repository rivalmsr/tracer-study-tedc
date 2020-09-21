from django.db import models


class MasterPoltekTedc(models.Model):
    kode            = models.CharField(
                        max_length=6,
                        default='045016',
    )
    nama            = models.CharField(max_length=100)
    status          = models.CharField(max_length=5, default='Aktif')
    email           = models.EmailField(blank=True)
    website         = models.CharField(max_length=100, blank=True)
    kota            = models.CharField(max_length=100)
    alamat          = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.kode, self.nama)

class MasterProdi(models.Model):
    kode            = models.PositiveIntegerField()
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
        ('D1', 'Diploma 1 (Satu)'),
        ('D3', 'Diploma 3 (Tiga)'),
        ('D4', 'Diploma 4 (Empat)'),
    )

    jenjang          = models.CharField(
                        max_length=2,
                        choices=LIST_DIPLOMA,
    )
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ['nama']

    def __str__(self):
        return "%s - %s" % (self.kode, self.nama)

