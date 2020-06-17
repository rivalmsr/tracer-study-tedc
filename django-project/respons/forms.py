from django import forms
from django.db.models.functions import Lower
from .models import (
    ResponsHeader,
    ResponsFDuaDetail,
)

from kuesioner.models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterOpsiRespons,
)

class ResponsHeaderForm(forms.Form):
    respons_f1 = forms.IntegerField(
        label = 'Nomor Mahasiswa'
        )

class ResponsFDuaForm(forms.Form):
    
    # Get Label Subkuesioner
    LIST_SUBKUESIONER = {}
    data_subkuesioner = MasterSubKuesioner.objects.values_list('kode', 'sub_pertanyaan')
    for kode, sub_pertanyaan in data_subkuesioner:
        LIST_SUBKUESIONER[kode] = sub_pertanyaan

    # Get Choices Respons
    CHOICES_F2 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F2').values_list( 'opsi_respons', 'opsi_respons')
    
    respons_f21 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-1'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )
    respons_f22 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-2'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )
    respons_f23 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-3'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )
    respons_f24 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-4'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )
    respons_f25 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-5'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )
    respons_f26 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-6'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )
    respons_f27 = forms.ChoiceField(
        label   = LIST_SUBKUESIONER['F2-7'],
        widget  = forms.RadioSelect,
        choices = CHOICES_F2,
        )


class ResponsFTigaForm(forms.Form):
    respons_f31 = forms.IntegerField()

    # Get Choices Respons
    CHOICES_F32 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F3').values_list('opsi_respons', 'opsi_respons')
    respons_f32 = forms.ChoiceField(
        widget  = forms.RadioSelect,
        choices = CHOICES_F32,   
    )


class ResponsFEmpatForm(forms.Form):
    CHOICES_F4  = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F4').values_list('opsi_respons', 'opsi_respons')
    respons_f4  = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
        choices = CHOICES_F4,
    )

class ResponsFLimaForm(forms.Form):
    respons_f51 = forms.IntegerField()

    # Get Choices Respons
    CHOICES_F52 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F5').values_list('opsi_respons', 'opsi_respons')
    respons_f52 = forms.ChoiceField(
        widget  = forms.RadioSelect,
        choices = CHOICES_F52,   
    )

class ResponsFEnamForm(forms.Form):
    LABEL_F6    = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F6').values_list('sub_pertanyaan', flat=True)
    respons_f6  = forms.IntegerField(
                    label=LABEL_F6[0],
    )

class ResponsFTujuhForm(forms.Form):
    LABEL_F7    = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F7').values_list('sub_pertanyaan', flat=True)
    respons_f7  = forms.IntegerField(
                    label=LABEL_F7[0],
    )

class ResponsFTujuhAForm(forms.Form):
    LABEL_F7A    = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F7A').values_list('sub_pertanyaan', flat=True)
    respons_f7A  = forms.IntegerField(
                    label=LABEL_F7A[0],
    )

class ResponsFDelapanForm(forms.Form):
    # Get Choices Respons
    CHOICES_F8 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F8').values_list('opsi_respons', 'opsi_respons')
    respons_f8 = forms.ChoiceField(
        widget  = forms.RadioSelect,
        choices = CHOICES_F8,   
    )

class ResponsFSembilanForm(forms.Form):
    CHOICES_F9  = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F9').values_list('opsi_respons', 'opsi_respons')
    respons_f9  = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
        choices = CHOICES_F9,
    )

class ResponsFSepuluhForm(forms.Form):
    # Get Choices Respons
    CHOICES_F10 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F10').values_list('opsi_respons', 'opsi_respons')
    respons_f10 = forms.ChoiceField(
        widget  = forms.RadioSelect,
        choices = CHOICES_F10,   
    )