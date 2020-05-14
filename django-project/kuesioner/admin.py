from django.contrib import admin
from .models import (
    MasterKuesioner, 
    MasterFSatu,
    MasterFDua
    )

class AdminMasterFSatu(admin.ModelAdmin):
    readonly_fields = ['kode_pt', 'created', 'updated']

admin.site.register(MasterFSatu, AdminMasterFSatu)

class AdminKuesioner(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
list_model = (
    MasterKuesioner, 
    MasterFDua
)
admin.site.register(list_model, AdminKuesioner)