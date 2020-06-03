from django.db import models
from django.utils.text import slugify
from kuesioner.models import MasterFSatu

class BiodataLulusan(models.Model):
    master_fsatu_id     = models.ForeignKey(MasterFSatu,
                            on_delete=models.CASCADE
    )
    tanggal_lahir       = models.DateField()
    jenis_kelamin       = models.CharField(max_length=12)
    verifikasi_email    = models.NullBooleanField(default=False)
    angkatan            = models.SmallIntegerField()
    pekerjaan           = models.CharField(max_length=100)
    alamat              = models.TextField()
    slug                = models.SlugField(blank=True, editable=False)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def save(self):
        self.slug = slugify(self.master_fsatu_id)
        super().save()

    def __str__(self):
        return "%s - %s" % (self.master_fsatu_id)