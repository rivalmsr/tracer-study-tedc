from django import forms
from .models import MasterFSatu

class MasterFSatuForm(forms.ModelForm):
    class Meta:
        model = MasterFSatu
        fields = [
            'nomor_mahasiswa',
            'tahun_lulus',
            'kode_prodi',
            'nama',
            'nomor_telepon',
            'alamat_email',
            ]