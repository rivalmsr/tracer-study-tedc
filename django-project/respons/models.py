from django.db import models
from django.utils.text import slugify
from kuesioner.models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterFSatu,
    MasterOpsiRespons,
)

class ResponsHeader(models.Model):
    master_fsatu_id         = models.ForeignKey(
                                MasterFSatu,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,    
    )
    completed               = models.BooleanField(default=False)
    current_tab             = models.SmallIntegerField(default=0)
    created                 = models.DateTimeField(auto_now_add=True)
    updated                 = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(blank=True, editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.master_fsatu_id)
        super(ResponsHeader, self).save(**kwargs)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.master_fsatu_id, self.completed)


class ResponsFDuaDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,

    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.CharField(
                                max_length=25,
                                blank=True,
                                null=True,
                                default=0,
                                
    )

    def save(self, **kwargs):
        super(ResponsFDuaDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)
    

class ResponsFTigaDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
    )
    keterangan              = models.CharField(
                                max_length=30,
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFTigaDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s %s" % (self.master_kuesioner_id, self.respons, self.keterangan)



class ResponsFEmpatDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.TextField(
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFEmpatDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFLimaDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
                                
    )
    keterangan              = models.CharField(
                                max_length=30,
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFLimaDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFEnamDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFEnamDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)



class ResponsFTujuhDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFTujuhDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFTujuhADetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFTujuhADetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFDelapanDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.CharField(
                                max_length=6,
                                blank=True,
                                null=True,
                                
    )
    
    def save(self, **kwargs):
        super(ResponsFDelapanDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFSembilanDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.TextField(
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFSembilanDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFSepuluhDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.CharField(
                                max_length=100,
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFSepuluhDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFSebelasDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.CharField(
                                max_length=100,
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFSebelasDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFTigabelasDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.BigIntegerField(
                                blank=True,
                                null=True,
                                default=0,
                                
    )

    def save(self, **kwargs):
        super(ResponsFTigabelasDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFEmpatbelasDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.CharField(
                                max_length=25,
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFEmpatbelasDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFLimabelasDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.CharField(
                                max_length=25,
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFLimabelasDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFEnambelasDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.TextField(
                                blank=True,
                                null=True,
                                
    )

    def save(self, **kwargs):
        super(ResponsFEnambelasDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_kuesioner_id, self.respons)


class ResponsFTujuhbelasADetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
                                default=0,
    )

    def save(self, **kwargs):
        super(ResponsFTujuhbelasADetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFTujuhbelasBDetail(models.Model):
    master_kuesioner_id     = models.ForeignKey(
                                MasterKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True
    )
    master_subkuesioner_id  = models.ForeignKey(
                                MasterSubKuesioner,
                                models.SET_NULL,
                                blank=True,
                                null=True,
    )
    respons_header_id       = models.ForeignKey(
                                ResponsHeader,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
    )
    respons                 = models.SmallIntegerField(
                                blank=True,
                                null=True,
                                default=0,
    )

    def save(self, **kwargs):
        super(ResponsFTujuhbelasBDetail, self).save(**kwargs)

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)