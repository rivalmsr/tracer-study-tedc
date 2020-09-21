from django import forms
from .models import BiodataLulusan

class BiodataLulusanForm(forms.ModelForm):
    class Meta:
        model = BiodataLulusan
        fields = [
            'tanggal_lahir',
            'jenis_kelamin',
            'status',
            'pendidikan_terakhir',
            'angkatan',
            'pekerjaan',
            'alamat',
            'foto',
            'akun_linkedin',
        ]

        widgets = {
            'tanggal_lahir': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class': 'form-control',
                }
            ),
            'jenis_kelamin': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'pendidikan_terakhir': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'angkatan': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'alamat': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'custom-file-input',
                }
            ),
            'akun_linkedin': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }