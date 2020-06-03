from django.db import models
from django.utils.text import slugify
from kuesioner.models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterFSatu,
)

class ResponsHeader(models.Model):
    master_fsatu_id         = models.ForeignKey(
                                MasterFSatu,
                                models.SET_NULL,
                                blank=True,
                                null=True,    
    )
    created                 = models.DateTimeField(auto_now_add=True)
    updated                 = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.master_fsatu_id)
        super().save()

    def __str__(self):
        return "%s - %s" % (self.id, self.master_fsatu_id)


class ResponsFDuaDetail(models.Model):
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
    respons                 = models.CharField(
                                max_length=25,
    )

    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)
    

class ResponsFTigaDetail(models.Model):
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
    respons                 = models.SmallIntegerField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)



class ResponsFEmpatDetail(models.Model):
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
    respons                 = models.TextField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFLimaDetail(models.Model):
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
    respons                 = models.SmallIntegerField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


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
                                null=True,
    )
    respons                 = models.SmallIntegerField()
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
    respons                 = models.SmallIntegerField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFDelapanDetail(models.Model):
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
    respons                 = models.CharField(max_length=6)
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFSembilanDetail(models.Model):
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
    respons                 = models.TextField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFSepuluhDetail(models.Model):
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
    respons                 = models.CharField(max_length=100)
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFSebelasDetail(models.Model):
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
    respons                 = models.CharField(max_length=100)
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)



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
    respons                 = models.BigIntegerField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)



class ResponsFEmpatbelasDetail(models.Model):
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
    respons                 = models.CharField(max_length=25)
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFLimabelasDetail(models.Model):
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
    respons                 = models.CharField(max_length=25)
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFEnambelasDetail(models.Model):
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
    respons                 = models.TextField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)


class ResponsFTujuhbelasDetail(models.Model):
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
    respons                 = models.SmallIntegerField()
    def __str__(self):
        return "%s - %s" % (self.master_subkuesioner_id, self.respons)