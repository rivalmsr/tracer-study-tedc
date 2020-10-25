import datetime
from django.db import models
from django.utils.text import slugify
from kuesioner.models import MasterFSatu

class BiodataLulusan(models.Model):
    master_fsatu_id     = models.ForeignKey(MasterFSatu,
                            on_delete=models.CASCADE
    )
    
    tanggal_lahir       = models.DateField(
                            blank=True, 
                            null=True,
    )
    
    LIST_JENIS_KELAMIN = (
        ('Perempuan', 'Perempuan'),
        ('Laki-laki', 'Laki-laki'),
        )
    jenis_kelamin       = models.CharField(
                            max_length=12,
                            choices=LIST_JENIS_KELAMIN,
                            blank=True,
                            default='-belum diisi-',
    )
    LIST_JENIS_STATUS = (
        ('Lajang', 'Lajang'),
        ('Sudah Menikah', 'Sudah Menikah')
    )
    status              = models.CharField(
                            max_length=15,
                            choices=LIST_JENIS_STATUS,
                            blank=True,
                            default='-belum diisi-',
    )
    pendidikan_terakhir = models.CharField(
                            max_length=255, 
                            blank=True,
                            default='-belum diisi-',
    )
    angkatan            = models.CharField(
                            max_length=5, 
                            blank=True,
                            null=True,
    )
    pekerjaan           = models.CharField(
                            max_length=100, 
                            blank=True,
                            default='-belum diisi-',
    )
    alamat              = models.TextField(
                            blank=True,
                            default='-belum diisi-',
    )
    foto                = models.ImageField(blank=True)
    akun_linkedin      = models.CharField(
                            max_length=255, 
                            blank=True,
                            default='-belum diisi-',
    )
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        self.slug = slugify(self.master_fsatu_id)

        super(BiodataLulusan, self).save(**kwargs)


    def __str__(self):
        return "%s" % (self.master_fsatu_id)