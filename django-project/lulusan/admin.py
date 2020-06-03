from django.contrib import admin
from .models import BiodataLulusan

class AdminBiodataLulusan(admin.ModelAdmin):
    readonly_fields = ['slug', 'created', 'updated']
admin.site.register(BiodataLulusan)
