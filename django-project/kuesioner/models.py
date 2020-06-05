from django.db import models
from django.urls import reverse
from datetime import datetime
from poltektedc.models import MasterProdi
from django.utils.text import slugify
from .validators import (
    validate_nomor_mahasiswa,
    validate_alamat_email,
)


class MasterKuesioner(models.Model):
    kode                = models.CharField(max_length=5)
    pertanyaan          = models.CharField(max_length=130)
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
    sub_pertanyaan      = models.CharField(max_length=35)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "%s - %s" % (self.kode, self.sub_pertanyaan)


class MasterOpsiRespons(models.Model):
    master_kuesioner_id = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    kode                = models.CharField(max_length=7)
    opsi_respons        = models.TextField()
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
    kode_pt             = models.PositiveIntegerField(default='045016', editable=False)
    
    LIST_OF_YEAR = []
    for y in range(2004, (datetime.now().year+1)):
        LIST_OF_YEAR.append((y, y))

    tahun_lulus         = models.PositiveSmallIntegerField(
                            choices=LIST_OF_YEAR,
    )
    
    LIST_OF_KODE_PRODI = []
    list_prodi = MasterProdi.objects.values_list('kode', 'nama')
    for i in list_prodi:
        LIST_OF_KODE_PRODI.append(i)
    kode_prodi          = models.PositiveSmallIntegerField(
                            choices=LIST_OF_KODE_PRODI,
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
