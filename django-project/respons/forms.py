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
    CHOICES_F52 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F3').values_list('opsi_respons', 'opsi_respons')
    respons_f52 = forms.ChoiceField(
        widget  = forms.RadioSelect,
        choices = CHOICES_F52,   
    )