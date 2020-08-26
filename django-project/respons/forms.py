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
        label  = 'Nomor Mahasiswa'
        )

class ResponsFDuaForm(forms.Form):
    
    # Get Label Subkuesioner
    LIST_SUBKUESIONER = {}
    data_subkuesioner = MasterSubKuesioner.objects.values_list('kode', 'sub_pertanyaan')
    for kode, sub_pertanyaan in data_subkuesioner:
        LIST_SUBKUESIONER[kode] = sub_pertanyaan

    # Get Choices Respons
    CHOICES_F2 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F2').values_list( 'opsi_respons', 'opsi_respons')
    
    respons_f2_1 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-1'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices  = CHOICES_F2,
        )
    respons_f2_2 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-2'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices  = CHOICES_F2,
        )
    respons_f2_3 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-3'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices  = CHOICES_F2,
        )
    respons_f2_4 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-4'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices  = CHOICES_F2,
        )
    respons_f2_5 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-5'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices = CHOICES_F2,
        )
    respons_f2_6 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-6'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices = CHOICES_F2,
        )
    respons_f2_7 = forms.ChoiceField(
        label    = LIST_SUBKUESIONER['F2-7'],
        widget   = forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        }),
        choices = CHOICES_F2,
        )


class ResponsFTigaForm(forms.Form):
    respons_f3_1 = forms.IntegerField(
        required = False,
        widget   = forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm'
            }
        ))

    # Get Choices Respons
    CHOICES_F3_2 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F3').values_list('opsi_respons', 'opsi_respons')
    respons_f3_2 = forms.ChoiceField(
        widget   = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F3_2,   
    )


class ResponsFEmpatForm(forms.Form):
    CHOICES_F4  = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F4').values_list('opsi_respons', 'opsi_respons')
    respons_f4  = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F4,
    )

class ResponsFLimaForm(forms.Form):
    respons_f5_1 = forms.IntegerField(
        widget   = forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm'
            }
        )
    )

    # Get Choices Respons
    CHOICES_F5_2 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F5').values_list('opsi_respons', 'opsi_respons')
    respons_f5_2 = forms.ChoiceField(
        widget   = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F5_2,   
    )

class ResponsFEnamForm(forms.Form):
    LABEL_F6    = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F6').values_list('sub_pertanyaan', flat=True)
    respons_f6  = forms.IntegerField(
        label   = LABEL_F6[0],
        widget  = forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )

    )

class ResponsFTujuhForm(forms.Form):
    LABEL_F7    = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F7').values_list('sub_pertanyaan', flat=True)
    respons_f7  = forms.IntegerField(
        label   = LABEL_F7[0],
        widget  = forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

class ResponsFTujuhAForm(forms.Form):
    LABEL_F7_A    = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F7A').values_list('sub_pertanyaan', flat=True)
    respons_f7_a  = forms.IntegerField(
        label     = LABEL_F7_A[0],
        widget    = forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

class ResponsFDelapanForm(forms.Form):
    # Get Choices Respons
    CHOICES_F8 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F8').values_list('opsi_respons', 'opsi_respons')
    respons_f8 = forms.ChoiceField(
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F8,   
    )

class ResponsFSembilanForm(forms.Form):
    CHOICES_F9  = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F9').values_list('opsi_respons', 'opsi_respons')
    respons_f9  = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F9,
    )

class ResponsFSepuluhForm(forms.Form):
    # Get Choices Respons
    CHOICES_F10 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F10').values_list('opsi_respons', 'opsi_respons')
    respons_f10 = forms.ChoiceField(
        required    = False,
        widget      = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices     = CHOICES_F10,   
    )

class ResponsFSebelasForm(forms.Form):
    # Get Choices Respons
    CHOICES_F11 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F11').values_list('opsi_respons', 'opsi_respons')
    respons_f11 = forms.ChoiceField(
        required    = False,
        widget      = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices     = CHOICES_F11,   
    )

class ResponsFTigabelasForm(forms.Form):
    LIST_SUBKUESIONER = {}
    data_subkuesioner = MasterSubKuesioner.objects.values_list('kode', 'sub_pertanyaan')
    for key, value in data_subkuesioner:
        LIST_SUBKUESIONER[key] = value

    respons_f13_1  = forms.IntegerField(
        required    = False,
        label       = LIST_SUBKUESIONER['F13-1'],
        widget    = forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    respons_f13_2  = forms.IntegerField(
        required    = False,
        label       = LIST_SUBKUESIONER['F13-2'],
        widget    = forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    respons_f13_3  = forms.IntegerField(
        required    = False,
        label       = LIST_SUBKUESIONER['F13-3'],
        widget    = forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

class ResponsFEmpatbelasForm(forms.Form):
    # Get Choices Respons
    CHOICES_F14 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F14').values_list('opsi_respons', 'opsi_respons')
    respons_f14 = forms.ChoiceField(
        required    = False,
        widget      = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices     = CHOICES_F14,   
    )

class ResponsFLimabelasForm(forms.Form):
    # Get Choices Respons
    CHOICES_F15 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F15').values_list('opsi_respons', 'opsi_respons')
    respons_f15 = forms.ChoiceField(
        required    = False,
        widget      = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices     = CHOICES_F15,   
    )


class ResponsFEnambelasForm(forms.Form):
    CHOICES_F16 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F16').values_list('opsi_respons', 'opsi_respons')
    respons_f16 = forms.MultipleChoiceField(
        required    = False,
        widget      = forms.CheckboxSelectMultiple(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices     = CHOICES_F16,
    )

class ResponsFTujuhbelasAForm(forms.Form):
    #Get Subkuesioner
    LIST_SUBKUESIONER = {}
    data_subkuesioner = MasterSubKuesioner.objects.values_list('kode', 'sub_pertanyaan')
    for key, value in data_subkuesioner:
        LIST_SUBKUESIONER[key] = value
    # Get Opsi Respons
    CHOICES_F17 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F17A').values_list('opsi_respons', 'opsi_respons')
    
    # Get respons forms
    list_form = [
        (1, 'F17-1'),
        (2, 'F17-2'),
    ]
    respons_f17_1_a = forms.ChoiceField(
            label   = LIST_SUBKUESIONER['F17-1'],
            widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
            choices = CHOICES_F17,
        )

    respons_f17_2_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-2'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_3_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-3'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_4_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-4'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_5_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-5'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_6_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-6'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_7_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-7'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_8_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-8'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_9_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-9'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_10_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-10'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_11_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-11'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_12_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-12'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_13_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-13'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_14_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-14'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_15_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-15'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_16_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-16'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_17_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-17'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_18_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-18'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_19_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-19'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_20_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-20'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_21_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-21'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_22_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-22'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_23_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-23'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_24_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-24'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_25_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-25'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_26_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-26'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_27_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-27'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_28_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-28'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_29_a = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-29'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

class ResponsFTujuhbelasBForm(forms.Form):
    #Get Subkuesioner
    LIST_SUBKUESIONER = {}
    data_subkuesioner = MasterSubKuesioner.objects.values_list('kode', 'sub_pertanyaan')
    for key, value in data_subkuesioner:
        LIST_SUBKUESIONER[key] = value
    # Get Opsi Respons
    CHOICES_F17 = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode='F17B').values_list('opsi_respons', 'opsi_respons')
    
    # Get respons forms
    list_form = [
        (1, 'F17-1'),
        (2, 'F17-2'),
    ]
    respons_f17_1_b = forms.ChoiceField(
            label   = LIST_SUBKUESIONER['F17-1'],
            widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
            choices = CHOICES_F17,
        )

    respons_f17_2_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-2'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_3_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-3'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_4_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-4'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_5_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-5'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_6_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-6'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_7_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-7'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_8_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-8'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_9_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-9'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_10_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-10'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_11_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-11'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_12_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-12'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_13_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-13'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_14_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-14'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_15_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-15'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_16_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-16'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_17_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-17'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_18_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-18'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_19_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-19'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_20_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-20'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_21_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-21'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_22_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-22'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_23_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-23'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_24_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-24'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_25_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-25'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_26_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-26'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_27_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-27'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_28_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-28'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )

    respons_f17_29_b = forms.ChoiceField(
        label   = LIST_SUBKUESIONER ['F17-29'],
        widget  = forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices = CHOICES_F17 
    )