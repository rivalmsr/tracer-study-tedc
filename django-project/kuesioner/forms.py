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
        widgets = {

            'nomor_mahasiswa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tahun_lulus': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'master_prodi_id': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nomor_telepon': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'alamat_email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),

        }