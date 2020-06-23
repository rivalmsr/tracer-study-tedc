from django.contrib import admin
from .models import (
    ResponsHeader,
    ResponsFDuaDetail,
    ResponsFTigaDetail,
    ResponsFEmpatDetail,
    ResponsFLimaDetail,
    ResponsFEnamDetail,
    ResponsFTujuhDetail,
    ResponsFTujuhADetail,
    ResponsFDelapanDetail,
    ResponsFSembilanDetail,
    ResponsFSepuluhDetail,
    ResponsFSebelasDetail,
    ResponsFTigabelasDetail,
    ResponsFEmpatbelasDetail,
    ResponsFLimabelasDetail,
    ResponsFEnambelasDetail,
    ResponsFTujuhbelasADetail,
    ResponsFTujuhbelasBDetail,
)

List_Respons_Model = (
    ResponsFDuaDetail,
    ResponsFTigaDetail,
    ResponsFEmpatDetail,
    ResponsFLimaDetail,
    ResponsFEnamDetail,
    ResponsFTujuhDetail,
    ResponsFTujuhADetail,
    ResponsFDelapanDetail,
    ResponsFSembilanDetail,
    ResponsFSepuluhDetail,
    ResponsFSebelasDetail,
    ResponsFTigabelasDetail,
    ResponsFEmpatbelasDetail,
    ResponsFLimabelasDetail,
    ResponsFEnambelasDetail,
    ResponsFTujuhbelasADetail,
    ResponsFTujuhbelasBDetail,
)
class AdminRespons(admin.ModelAdmin):
    readonly_fields = ['slug', 'created', 'updated']

admin.site.register(ResponsHeader, AdminRespons)
admin.site.register(List_Respons_Model)