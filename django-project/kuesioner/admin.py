from django.contrib import admin
from .models import (
    MasterKuesioner, 
    MasterFSatu,
    MasterSubKuesioner
    )

class AdminMasterFSatu(admin.ModelAdmin):
    readonly_fields = ['kode_pt', 'slug', 'created', 'updated']

admin.site.register(MasterFSatu, AdminMasterFSatu)

class AdminKuesioner(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
list_model = (
    MasterKuesioner, 
    MasterSubKuesioner
)
admin.site.register(list_model, AdminKuesioner)