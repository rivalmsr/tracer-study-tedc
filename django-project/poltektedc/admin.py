from django.contrib import admin
from .models import (
    MasterPoltekTedc,
    MasterProdi
)

class AdminPoltekTedc(admin.ModelAdmin):
    readonly_fields = ['kode', 'status', 'created', 'updated']
admin.site.register(MasterPoltekTedc, AdminPoltekTedc)

List_Model = (
    MasterProdi,
)
class AdminPoltek(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
admin.site.register(List_Model, AdminPoltek)
