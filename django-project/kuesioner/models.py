from django.db import models
from django.urls import reverse
from datetime import datetime
from poltektedc.models import ( 
    MasterPoltekTedc,
    MasterProdi,
)
from django.utils.text import slugify
from .validators import (
    validate_nomor_mahasiswa,
    validate_alamat_email,
)


class MasterKuesioner(models.Model):
    kode                = models.CharField(max_length=5)
    pertanyaan          = models.CharField(max_length=150)
    keterangan          = models.TextField(blank=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['id']

    def __str__(self):
        return "%s - %s " % (self.kode, self.pertanyaan)


class MasterSubKuesioner(models.Model):
    master_kuesioner_id = models.ManyToManyField(
                                MasterKuesioner,
                                blank=True,
    )
    kode                = models.CharField(max_length=7)
    sub_pertanyaan      = models.CharField(max_length=150)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "%s - %s" % (self.kode, self.sub_pertanyaan)


class MasterOpsiRespons(models.Model):
    master_kuesioner_id = models.ManyToManyField(
                                MasterKuesioner,
                                blank=True,
    )
    kode                = models.CharField(max_length=7)
    opsi_respons        = models.CharField(max_length=150)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "%s - %s" %(self.kode, self.opsi_respons)


class MasterFSatu(models.Model):
    nomor_mahasiswa     = models.CharField(
                            max_length=12,
                            unique=True)
    DEFAULT_POLTEK = 1
    master_poltek_id    = models.ForeignKey(
                        MasterPoltekTedc,
                        models.SET_NULL,
                        blank=True,
                        null=True,
                        default=DEFAULT_POLTEK,
    )
    master_prodi_id     = models.ForeignKey(
                        MasterProdi,
                        models.SET_NULL,
                        blank=True,
                        null=True,
    )
    LIST_OF_YEAR = []
    for y in range(2018, (datetime.now().year+1)):
        LIST_OF_YEAR.append((y, y))

    tahun_lulus         = models.PositiveSmallIntegerField(
                            choices=LIST_OF_YEAR,
    )
    nama                = models.CharField(max_length=100)
    nomor_telepon       = models.CharField(max_length=13)
    alamat_email        = models.EmailField()
    slug                = models.SlugField(blank=True, editable=False)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def save(self):
        text_slug = self.nomor_mahasiswa +' '+self.nama
        self.slug = slugify(text_slug)
        
        return super().save()

    def get_absolute_url(self):
        return reverse('lulusan:create')

    def __str__(self):
        return "%s - %s" % (self.nomor_mahasiswa, self.nama)
