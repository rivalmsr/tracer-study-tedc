from django.db import models


class MasterKuesioner(models.Model):
    kode                = models.CharField(max_length=5)
    judul               = models.CharField(max_length=120)
    deskripsi           = models.TextField(blank=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.kode, self.judul)


class MasterFSatu(models.Model):
    nomor_mahasiswa     = models.CharField(max_length=12)
    kode_pt             = models.IntegerField(default='045016', editable=False)
    tahun_lulusan       = models.SmallIntegerField()
    kode_prodi          = models.SmallIntegerField()
    nama                = models.CharField(max_length=100)
    nomor_telepon       = models.SmallIntegerField()
    alamat_email        = models.EmailField()
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.nomor_mahasiswa, self.nama)



class MasterFDua(models.Model):
    master_kuesioner    = models.ForeignKey(
                            MasterKuesioner, 
                            models.SET_NULL,
                            blank=True,
                            null=True
                        )
    pertanyaan          = models.CharField(max_length=35)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s | %s" % (self.master_kuesioner, self.pertanyaan)

