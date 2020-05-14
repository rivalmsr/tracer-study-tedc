from django.contrib import admin
from .models import (
    MasterPoltekTedc,
    MasterProdi
)

class AdminPoltek(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

List_Model = (
    MasterPoltekTedc,
    MasterProdi,
)

admin.site.register(List_Model, AdminPoltek)
