from django.contrib import admin
from .models import (
    MasterKuesioner, 
    MasterSubKuesioner,
    MasterOpsiRespons,
    MasterFSatu,
    )

class AdminMasterFSatu(admin.ModelAdmin):
    readonly_fields = ['kode_pt', 'slug', 'created', 'updated']

admin.site.register(MasterFSatu, AdminMasterFSatu)

class AdminKuesioner(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
list_model = (
    MasterKuesioner, 
    MasterSubKuesioner,
    MasterOpsiRespons
)
admin.site.register(list_model, AdminKuesioner)