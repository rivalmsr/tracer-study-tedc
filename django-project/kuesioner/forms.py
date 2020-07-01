from django import forms
from .models import MasterFSatu

class MasterFSatuForm(forms.ModelForm):
    class Meta:
        model = MasterFSatu
        fields = [
            'nomor_mahasiswa',
            'master_poltek_id',
            'master_prodi_id',
            'tahun_lulus',
            'nama',
            'nomor_telepon',
            'alamat_email',
            ]
        