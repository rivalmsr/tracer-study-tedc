from django import forms
from kuesioner.models import MasterFSatu
from poltektedc.models import MasterProdi

class ReportHorizontalAndVerticalForm(forms.Form):
    kode_pt = forms.CharField()

    try:
        # get prodi from database
        CHOICES_PRODI = MasterFSatu.objects.values_list('master_prodi_id__nama', 'master_prodi_id__nama').distinct()
        prodi   = forms.ChoiceField(
                    choices = CHOICES_PRODI,
        )
    except:
        CHOICES_PRODI = MasterProdi.objects.values_list('nama', 'nama').distinct()
        prodi   = forms.ChoiceField(
                    choices = CHOICES_PRODI,
        )

    try:
        # get lulusan from database
        CHOICES_TAHUN_LULUSAN = MasterFSatu.objects.values_list('tahun_lulus','tahun_lulus').distinct()
        tahun_lulus = forms.ChoiceField(
                    choices = CHOICES_TAHUN_LULUSAN,
        )    
    except:
        tahun_lulus = forms.CharField()
    
