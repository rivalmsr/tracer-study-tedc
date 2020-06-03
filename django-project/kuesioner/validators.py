from django.core.exceptions import ValidationError


def validate_nomor_mahasiswa(value):
    from .models import MasterFSatu
    if MasterFSatu.objects.filter(nomor_mahasiswa=value).exists():
        message =  "Maaf nomor mahasiswa "+ value +" sudah terdaftar!"
        raise ValidationError(message)

def validate_alamat_email(value):
    from .models import MasterFSatu
    if MasterFSatu.objects.filter(alamat_email=value).exists():
        message =  "Maaf alamat email "+ value +" sudah digunakan!"
        raise ValidationError(message)