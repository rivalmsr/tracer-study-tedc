from django.shortcuts import render, redirect

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import (
    ResponsHeader,
    ResponsFDuaDetail,
    ResponsFTigaDetail,
    ResponsFEmpatDetail,
    ResponsFLimaDetail,
    ResponsFEnamDetail,
    ResponsFTujuhDetail,
    ResponsFTujuhADetail,
    ResponsFDelapanDetail,
    ResponsFSembilanDetail,
    ResponsFSepuluhDetail,
    ResponsFSebelasDetail,
    ResponsFTigabelasDetail,
    ResponsFEmpatbelasDetail,
    ResponsFLimabelasDetail,
    ResponsFEnambelasDetail,
    ResponsFTujuhbelasADetail,
    ResponsFTujuhbelasBDetail,
)

from .forms import (
    ResponsHeaderForm,
    ResponsFDuaForm,
    ResponsFTigaForm,
    ResponsFEmpatForm,
    ResponsFLimaForm,
    ResponsFEnamForm,
    ResponsFTujuhForm,
    ResponsFTujuhAForm,
    ResponsFDelapanForm,
    ResponsFSembilanForm,
    ResponsFSepuluhForm,
    ResponsFSebelasForm,
    ResponsFTigabelasForm,
    ResponsFEmpatbelasForm,
    ResponsFLimabelasForm,
    ResponsFEnambelasForm,
    ResponsFTujuhbelasAForm,
    ResponsFTujuhbelasBForm,
)

from kuesioner.views import KuesionerForm

from kuesioner.models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterOpsiRespons,
    MasterFSatu,
)


def index(request):
    template_name = 'respons/respons_index.html'
    context = {
        'title': 'Index Respons'
    }
    return render(request, template_name, context)

class ResponsListView(ListView):
    model = ResponsHeader
    template_name   = 'respons/respons_list.html'
    context_object_name = 'list_of_responden'
    extra_context= {
        'title': 'List Responden'
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

def create(request):  
    # Initialisasi Dictionary 
    context = {}
    
    # Returns to template
    template_name       = 'respons/respons_form.html'
    context['title']    = 'Create Respons'    

    # Get Kuesioner 
    key_context_kuesioner = 'kuesioner_'
    list_kode_kuesioner = MasterKuesioner.objects.values_list('kode', flat=True)
    for kode in list_kode_kuesioner:
        context[key_context_kuesioner+kode] = MasterKuesioner.objects.filter(kode=kode)
    
    # Respons Form
    header_form         = ResponsHeaderForm(request.POST or None)
    fdua_form           = ResponsFDuaForm(request.POST or None)
    ftiga_form          = ResponsFTigaForm(request.POST or None)
    fempat_form         = ResponsFEmpatForm(request.POST or None)
    flima_form          = ResponsFLimaForm(request.POST or None)
    fenam_form          = ResponsFEnamForm(request.POST or None)
    ftujuh_form         = ResponsFTujuhForm(request.POST or None)
    ftujuh_a_form       = ResponsFTujuhAForm(request.POST or None)
    fdelapan_form       = ResponsFDelapanForm(request.POST or None)
    fsembilan_form      = ResponsFSembilanForm(request.POST or None)
    fsepuluh_form       = ResponsFSepuluhForm(request.POST or None)
    fsebelas_form       = ResponsFSebelasForm(request.POST or None)
    ftigabelas_form     = ResponsFTigabelasForm(request.POST or None)
    fempatbelas_form    = ResponsFEmpatbelasForm(request.POST or None)
    flimabelas_form     = ResponsFLimabelasForm(request.POST or None)
    fenambelas_form     = ResponsFEnambelasForm(request.POST or None)
    ftujuhbelas_a_form  = ResponsFTujuhbelasAForm(request.POST or None)
    ftujuhbelas_b_form  = ResponsFTujuhbelasBForm(request.POST or None)
    

    # List key context and forms
    list_form = [
        ('header_form', header_form),
        ('fdua_form', fdua_form),
        ('ftiga_form', ftiga_form),
        ('fempat_form', fempat_form),
        ('flima_form', flima_form),
        ('fenam_form', fenam_form),        
        ('ftujuh_form', ftujuh_form),
        ('ftujuh_a_form', ftujuh_a_form),
        ('fdelapan_form', fdelapan_form),
        ('fsembilan_form', fsembilan_form),
        ('fsepuluh_form', fsepuluh_form),
        ('fsebelas_form', fsebelas_form),
        ('ftigabelas_form', ftigabelas_form),
        ('fempatbelas_form', fempatbelas_form),
        ('flimabelas_form', flimabelas_form),
        ('fenambelas_form', fenambelas_form),
        ('ftujuhbelas_a_form', ftujuhbelas_a_form),
        ('ftujuhbelas_b_form', ftujuhbelas_b_form),
    ]  

    # Return forms to context
    for key, value in list_form:
        context[key] = value

    # Reqeust Method Check
    if request.method == 'POST':
        if header_form.is_valid():
            fsatu = ResponsHeader.objects.create( 
                master_fsatu_id = MasterFSatu.objects.get(pk=request.POST.get('respons_f1')) 
            )
            fsatu.save()
            
            if  ResponsHeader.objects.filter(master_fsatu_id__pk=request.POST.get('respons_f1')).exists():
                # Respons F2
                if fdua_form.is_valid():
                    data_fdua = {}

                    # Get and Return request to dictionary
                    for number in range(1, 8):
                        data_fdua["F2-" + str(number)] = request.POST.get("respons_f2_"+ str(number)) 

                    # Save data into database
                    for key, value in data_fdua.items():
                        fdua = ResponsFDuaDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f2')),
                            master_subkuesioner_id  = MasterSubKuesioner.objects.get(kode=key),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = value
                        )
                        fdua.save()

                # Respons F3
                if ftiga_form.is_valid():
                    ftiga = ResponsFTigaDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f3')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f3_1'),
                        keterangan              = request.POST.get('respons_f3_2')
                    )
                    ftiga.save()

                # Respons F4
                if fempat_form.is_valid():
                    fempat = ResponsFEmpatDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f4')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.getlist('respons_f4')
                    )
                    ftiga.save()
                    
                # Respons F5
                if flima_form.is_valid():
                    flima = ResponsFLimaDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f5')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f5_1'),
                        keterangan              = request.POST.get('respons_f5_2')
                    )
                    flima.save()

                # Respons F6
                if fenam_form.is_valid():
                    fenam = ResponsFEnamDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f6')),
                        master_subkuesioner_id  = MasterSubKuesioner.objects.get(master_kuesioner_id__pk=request.POST.get('kuesioner_f6')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f6'),
                    )
                    fenam.save()

                # Respons F7
                if ftujuh_form.is_valid():
                    ftujuh = ResponsFTujuhDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f7')),
                        master_subkuesioner_id  = MasterSubKuesioner.objects.get(master_kuesioner_id__pk=request.POST.get('kuesioner_f7')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f7'),
                    )
                    ftujuh.save()

                # Respons F7A
                if ftujuh_a_form.is_valid():
                    ftujuh_a = ResponsFTujuhADetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f7A')),
                        master_subkuesioner_id  = MasterSubKuesioner.objects.get(master_kuesioner_id__pk=request.POST.get('kuesioner_f7A')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f7_a'),
                    )
                    ftujuh_a.save()
                
                # Respons F8
                if fdelapan_form.is_valid():
                    fdelapan = ResponsFDelapanDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f8')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f8'),
                    )
                    fdelapan.save()
                
                # Check Condition if value F8 is Not
                if  request.POST.get('respons_f8') == MasterOpsiRespons.objects.values_list('opsi_respons', flat=True).get(kode='F8-02'):

                    # Respons F9
                    if fsembilan_form.is_valid():
                        fsembilan = ResponsFSembilanDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f9')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = request.POST.getlist('respons_f9'),
                        )
                        fsembilan.save()

                    # Respons F10
                    if fsepuluh_form.is_valid():
                        fsepuluh = ResponsFSepuluhDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f10')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = request.POST.get('respons_f10'),
                        )
                        fsepuluh.save()
                
                else:
                    # Respons F11
                    if fsebelas_form.is_valid():
                        fsebelas = ResponsFSebelasDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f11')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = request.POST.get('respons_f11'),
                        )
                        fsebelas.save()

                    # Respons F13
                    if ftigabelas_form.is_valid():
                        data_ftigabelas = {}

                        # Get and Return request to dictionary
                        for number in range(1, 4):
                            data_ftigabelas["F13-" + str(number)] = request.POST.get("respons_f13_"+ str(number)) 

                        for key, value in data_ftigabelas.items():
                            ftigabelas = ResponsFTigabelasDetail.objects.create(
                                master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f13')),
                                master_subkuesioner_id  = MasterSubKuesioner.objects.get(kode=key),
                                respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                                respons                 = value
                            )
                            ftigabelas.save()

                    # Respons F14
                    if fempatbelas_form.is_valid():
                        fempatbelas = ResponsFEmpatbelasDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f14')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = request.POST.get('respons_f14'),
                        )
                        fempatbelas.save()

                    # Respons F15
                    if flimabelas_form.is_valid():
                        flimabelas = ResponsFLimabelasDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f15')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = request.POST.get('respons_f15'),
                        )
                        flimabelas.save()

                    # Respons F16
                    if fenambelas_form.is_valid():
                        fenambelas = ResponsFEnambelasDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f16')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = request.POST.getlist('respons_f16'),
                        )
                        fenambelas.save()

                # Respons F17A
                if ftujuhbelas_a_form.is_valid():
                    data_ftujuhbelas_a = {}
                    # Get and Return request to dictionary
                    for number in range(1, 30):
                        data_ftujuhbelas_a["F17-" + str(number)] = request.POST.get("respons_f17_"+ str(number)+"_a") 
                    # Create data in dictionary to database
                    for key, value in data_ftujuhbelas_a.items():
                        ftujuhbelas_a = ResponsFTujuhbelasADetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f17A')),
                            master_subkuesioner_id  = MasterSubKuesioner.objects.get(kode=key),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = value
                        )
                        ftujuhbelas_a.save()

                # Respons F17B
                if ftujuhbelas_b_form.is_valid():
                    data_ftujuhbelas_b = {}
                    # Get and Return request to dictionary
                    for number in range(1, 30):
                        data_ftujuhbelas_b["F17-" + str(number)] = request.POST.get("respons_f17_"+ str(number)+"_b") 
                    # Create data in dictionary to database
                    for key, value in data_ftujuhbelas_b.items():
                        ftujuhbelas_b = ResponsFTujuhbelasBDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f17B')),
                            master_subkuesioner_id  = MasterSubKuesioner.objects.get(kode=key),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = value
                        )
                        ftujuhbelas_b.save()

    return render(request, template_name, context)

def update(request, update_id):
    template_name       = 'respons/respons_form.html'
    context             = {
        'title': 'Create Respons'
        }
    # Get Kuesioner 
    key_context_kuesioner = 'kuesioner_'
    list_kode_kuesioner = MasterKuesioner.objects.values_list('kode', flat=True)
    for kode in list_kode_kuesioner:
        context[key_context_kuesioner+kode] = MasterKuesioner.objects.filter(kode=kode)
    
    # Get value from database
    # Respons Form
    get_value_header_form = ResponsHeader.objects.get(pk=update_id)
    data_form_header = {
        'respons_f1': get_value_header_form.master_fsatu_id.pk
    }
    header_form         = ResponsHeaderForm(request.POST or None, initial=data_form_header)

    # F2
    get_value_fdua  = ResponsFDuaDetail.objects.filter(respons_header_id__pk=update_id).values_list('respons', flat=True).order_by('master_subkuesioner_id')
    data_form_fdua  = {}
    for number, respons in enumerate(get_value_fdua, 1):
        data_form_fdua['respons_f2_'+str(number)] = respons
    fdua_form       = ResponsFDuaForm(request.POST or None, initial=data_form_fdua)

    # F3
    get_value_ftiga = ResponsFTigaDetail.objects.get(respons_header_id__pk=update_id)
    data_form_ftiga = {
        'respons_f3_1': get_value_ftiga.respons,
        'respons_f3_2': get_value_ftiga.keterangan,
    }
    ftiga_form      = ResponsFTigaForm(request.POST or None, initial=data_form_ftiga)

    # F4
    get_value_fempat = ResponsFEmpatDetail.objects.get(respons_header_id__pk=update_id)
    data_form_fempat = {
        'respons_f4': get_value_fempat.respons
    }
    fempat_form     = ResponsFEmpatForm(request.POST or None, initial=data_form_fempat)

    # F5
    get_value_flima = ResponsFLimaDetail.objects.get(respons_header_id__pk=update_id)
    data_form_flima = {
        'respons_f5_1': get_value_flima.respons,
        'respons_f5_2': get_value_flima.keterangan,
    }
    flima_form      = ResponsFLimaForm(request.POST or None, initial=data_form_flima)

    # F6
    get_value_fenam = ResponsFEnamDetail.objects.get(respons_header_id__pk=update_id)
    data_form_fenam = {
        'respons_f6': get_value_fenam.respons,
    }
    fenam_form      = ResponsFEnamForm(request.POST or None, initial=data_form_fenam)

    # F7
    get_value_ftujuh = ResponsFTujuhDetail.objects.get(respons_header_id__pk=update_id)
    data_form_ftujuh = {
        'respons_f7': get_value_ftujuh.respons,
    }
    ftujuh_form      = ResponsFTujuhForm(request.POST or None, initial=data_form_ftujuh)

    # F7A
    get_value_ftujuh_a = ResponsFTujuhADetail.objects.get(respons_header_id__pk=update_id)

    # F7A
    data_form_ftujuh_a = {
        'respons_f7_a': get_value_ftujuh_a.respons,
    }
    ftujuh_a_form      = ResponsFTujuhAForm(request.POST or None, initial=data_form_ftujuh_a)

    # F8
    get_value_fdelapan = ResponsFDelapanDetail.objects.get(respons_header_id__pk=update_id)
    data_form_fdelapan = {
        'respons_f8': get_value_fdelapan.respons,
    }
    fdelapan_form      = ResponsFDelapanForm(request.POST or None, initial=data_form_fdelapan)

    # F9
    if ResponsFSembilanDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_fsembilan = ResponsFSembilanDetail.objects.get(respons_header_id__pk=update_id)
        data_form_fsembilan = {
            'respons_f9': get_value_fsembilan.respons
        }
        fsembilan_form     = ResponsFSembilanForm(request.POST or None, initial=data_form_fsembilan)
    else:
        fsembilan_form     = ResponsFSembilanForm(request.POST or None)

    # F10
    if ResponsFSepuluhDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_fsepuluh = ResponsFSepuluhDetail.objects.get(respons_header_id__pk=update_id)
        data_form_fsepuluh = {
            'respons_f10': get_value_fsepuluh.respons,   
        }
        fsepuluh_form      = ResponsFSepuluhForm(request.POST or None, initial=data_form_fsepuluh)
    else:
        fsepuluh_form      = ResponsFSepuluhForm(request.POST or None)

    # F11
    if ResponsFSebelasDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_fsebelas = ResponsFSebelasDetail.objects.get(respons_header_id__pk=update_id)
        data_form_fsebelas = {
            'respons_f11': get_value_fsebelas.respons,   
        }
        fsebelas_form      = ResponsFSebelasForm(request.POST or None, initial=data_form_fsebelas)
    else:
        fsebelas_form       = ResponsFSebelasForm(request.POST or None)
    
    # F13
    if ResponsFTigabelasDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_ftigabelas  = ResponsFTigabelasDetail.objects.filter(respons_header_id__pk=update_id).values_list('respons', flat=True).order_by('master_subkuesioner_id')
        data_form_ftigabelas  = {}
        for number, respons in enumerate(get_value_ftigabelas, 1):
            data_form_ftigabelas['respons_f13_'+str(number)] = respons
        ftigabelas_form       = ResponsFTigabelasForm(request.POST or None, initial=data_form_ftigabelas)
    else:
        ftigabelas_form       = ResponsFTigabelasForm(request.POST or None)

    # F14
    if ResponsFEmpatbelasDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_fempatbelas = ResponsFEmpatbelasDetail.objects.get(respons_header_id__pk=update_id)
        data_form_fempatbelas = {
            'respons_f14': get_value_fempatbelas.respons,   
        }
        fempatbelas_form      = ResponsFEmpatbelasForm(request.POST or None, initial=data_form_fempatbelas)
    else:
        fempatbelas_form       = ResponsFEmpatbelasForm(request.POST or None)

    # F15
    if ResponsFLimabelasDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_flimabelas = ResponsFLimabelasDetail.objects.get(respons_header_id__pk=update_id)
        data_form_flimabelas = {
            'respons_f15': get_value_flimabelas.respons,   
        }
        flimabelas_form      = ResponsFLimabelasForm(request.POST or None, initial=data_form_flimabelas)
    else:
        flimabelas_form       = ResponsFLimabelasForm(request.POST or None)

    # F16
    if ResponsFEnambelasDetail.objects.filter(respons_header_id__pk=update_id).exists():
        get_value_fenambelas = ResponsFEnambelasDetail.objects.get(respons_header_id__pk=update_id)
        data_form_fenambelas = {
            'respons_f16': get_value_fenambelas.respons,   
        }
        fenambelas_form      = ResponsFEnambelasForm(request.POST or None, initial=data_form_fenambelas)
    else:
        fenambelas_form       = ResponsFEnambelasForm(request.POST or None)

    # F17 A
    get_value_ftujuhbelas_a  = ResponsFTujuhbelasADetail.objects.filter(respons_header_id__pk=update_id).values_list('respons', flat=True).order_by('master_subkuesioner_id')
    data_form_ftujuhbelas_a  = {}
    for number, respons in enumerate(get_value_ftujuhbelas_a, 1):
        data_form_ftujuhbelas_a['respons_f17_'+str(number)+'_a'] = respons
    ftujuhbelas_a_form       = ResponsFTujuhbelasAForm(request.POST or None, initial=data_form_ftujuhbelas_a)

    # F17 B
    get_value_ftujuhbelas_b  = ResponsFTujuhbelasBDetail.objects.filter(respons_header_id__pk=update_id).values_list('respons', flat=True).order_by('master_subkuesioner_id')
    data_form_ftujuhbelas_b  = {}
    for number, respons in enumerate(get_value_ftujuhbelas_b, 1):
        data_form_ftujuhbelas_b['respons_f17_'+str(number)+'_b'] = respons
    ftujuhbelas_b_form       = ResponsFTujuhbelasBForm(request.POST or None, initial=data_form_ftujuhbelas_b)
    
    # List key context and forms
    list_form = [
        ('header_form', header_form),
        ('fdua_form', fdua_form),
        ('ftiga_form', ftiga_form),
        ('fempat_form', fempat_form),
        ('flima_form', flima_form),
        ('fenam_form', fenam_form),        
        ('ftujuh_form', ftujuh_form),
        ('ftujuh_a_form', ftujuh_a_form),
        ('fdelapan_form', fdelapan_form),
        ('fsembilan_form', fsembilan_form),
        ('fsepuluh_form', fsepuluh_form),
        ('fsebelas_form', fsebelas_form),
        ('ftigabelas_form', ftigabelas_form),
        ('fempatbelas_form', fempatbelas_form),
        ('flimabelas_form', flimabelas_form),
        ('fenambelas_form', fenambelas_form),
        ('ftujuhbelas_a_form', ftujuhbelas_a_form),
        ('ftujuhbelas_b_form', ftujuhbelas_b_form),
    ]  

    # Return forms to context
    for key, value in list_form:
        context[key] = value

    # Reqeust Method Check
    if request.method == 'POST':
        if ResponsHeader.objects.filter(master_fsatu_id__pk=request.POST.get('respons_f1')).exists():
            respons_header = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1'))
            
            # Respons F2
            if fdua_form.is_valid():
                get_fdua_id = ResponsFDuaDetail.objects.filter(respons_header_id__pk=respons_header.pk).values_list('pk', flat=True)
                data_fdua = {}
                # Get and Return request to dictionary
                for number, fdua_id in enumerate(get_fdua_id, 1):
                    data_fdua[fdua_id] = request.POST.get("respons_f2_"+ str(number)) 
                for key, value in data_fdua.items():
                    fdua = ResponsFDuaDetail.objects.filter(pk=key).update(
                        respons = value
                    )
            # Respons F3
            if ftiga_form.is_valid():
                get_ftiga = ResponsFTigaDetail.objects.get(respons_header_id__pk=respons_header.pk)
                ftiga = ResponsFTigaDetail.objects.filter(pk=get_ftiga.pk).update(
                    respons = request.POST.get('respons_f3_1'),
                    keterangan = request.POST.get('respons_f3_2')
                )
            # Respons F4
            if fempat_form.is_valid():
                get_fempat = ResponsFEmpatDetail.objects.get(respons_header_id__pk=respons_header.pk)
                fempat = ResponsFEmpatDetail.objects.filter(pk=get_fempat.pk).update(
                    respons = request.POST.getlist('respons_f4')
                )
            # Respons F5
            if flima_form.is_valid():
                get_flima = ResponsFLimaDetail.objects.get(respons_header_id__pk=respons_header.pk)
                flima = ResponsFLimaDetail.objects.filter(pk=get_flima.pk).update(
                    respons = request.POST.get('respons_f5_1'),
                    keterangan = request.POST.get('respons_f5_2')
                )
            # Respons F6
            if fenam_form.is_valid():
                get_fenam = ResponsFEnamDetail.objects.get(respons_header_id__pk=respons_header.pk)
                fenam = ResponsFEnamDetail.objects.filter(pk=get_fenam.pk).update(
                    respons = request.POST.get('respons_f6')
                )
            # Respons F7
            if ftujuh_form.is_valid():
                get_ftujuh = ResponsFTujuhDetail.objects.get(respons_header_id__pk=respons_header.pk)
                ftujuh = ResponsFTujuhDetail.objects.filter(pk=get_ftujuh.pk).update(
                    respons = request.POST.get('respons_f7')
                )
            # Respons F7A
            if ftujuh_a_form.is_valid():
                get_ftujuh_a = ResponsFTujuhADetail.objects.get(respons_header_id__pk=respons_header.pk)
                ftujuh_a = ResponsFTujuhADetail.objects.filter(pk=get_ftujuh_a.pk).update(
                    respons = request.POST.get('respons_f7_a')
                )
            # Respons F8
            if fdelapan_form.is_valid():
                get_fdelapan = ResponsFDelapanDetail.objects.get(respons_header_id__pk=respons_header.pk)
                fdelapan = ResponsFDelapanDetail.objects.filter(pk=get_fdelapan.pk).update(
                    respons = request.POST.get('respons_f8')
                )
            # Check Condition if value F8 is "Tidak"
            if  request.POST.get('respons_f8') == MasterOpsiRespons.objects.values_list('opsi_respons', flat=True).get(kode='F8-02'):
                # Respons F9
                if fsembilan_form.is_valid():
                    get_fsembilan = ResponsFSembilanDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fsembilan = ResponsFSembilanDetail.objects.filter(pk=get_fsembilan.pk).update(
                        respons = request.POST.getlist('respons_f9')
                    )
                # Respons F10
                if fsepuluh_form.is_valid():
                    get_fsepuluh = ResponsFSepuluhDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fsepuluh = ResponsFSepuluhDetail.objects.filter(pk=get_fsepuluh.pk).update(
                        respons = request.POST.get('respons_f10')
                    )
            else:
                # Respons F11
                if fsebelas_form.is_valid():
                    get_fsebelas = ResponsFSebelasDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fsebelas = ResponsFSebelasDetail.objects.filter(pk=get_fsebelas.pk).update(
                        respons = request.POST.get('respons_f11')
                    )
                # Respons F13
                if ftigabelas_form.is_valid():
                    get_ftigabelas_id = ResponsFTigabelasDetail.objects.filter(respons_header_id__pk=respons_header.pk).values_list('pk', flat=True)
                    data_ftigabelas = {}
                    # return pk and value request into dictionary
                    for number, ftigabelas_id in enumerate(get_ftigabelas_id, 1):
                        data_ftigabelas[ftigabelas_id] = request.POST.get('respons_f13_'+str(number))
                    # return database update each subkuesioner
                    for key, value in data_ftigabelas.items():
                        ftigabelas = ResponsFTigabelasDetail.objects.filter(pk=key).update(
                            respons = value
                        )
                # Respons F14
                if fempatbelas_form.is_valid():
                    get_fempatbelas = ResponsFEmpatbelasDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fempatbelas = ResponsFEmpatbelasDetail.objects.filter(pk=get_fempatbelas.pk).update(
                        respons = request.POST.get('respons_f14')
                    )
                # Respons F15
                if flimabelas_form.is_valid():
                    get_flimabelas = ResponsFLimabelasDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    flimabelas = ResponsFLimabelasDetail.objects.filter(pk=get_flimabelas.pk).update(
                        respons = request.POST.get('respons_f15')
                    )
                # Respons F16
                if fenambelas_form.is_valid():
                    get_fenambelas = ResponsFEnambelasDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fenambelas = ResponsFEnambelasDetail.objects.filter(pk=get_fenambelas.pk).update(
                        respons = request.POST.getlist('respons_f16')
                    )
            # Respons F17A
            if ftujuhbelas_a_form.is_valid():
                get_ftujuhbelas_a_id = ResponsFTujuhbelasADetail.objects.filter(respons_header_id__pk=respons_header.pk).values_list('pk', flat=True)
                data_ftujuhbelas_a = {}
                # Get and Return request to dictionary
                for number, ftujuhbelas_a_id in enumerate(get_ftujuhbelas_a_id, 1):
                    data_ftujuhbelas_a[ftujuhbelas_a_id] = request.POST.get("respons_f17_"+ str(number)+"_a")
                for key, value in data_ftujuhbelas_a.items():
                    fdua = ResponsFTujuhbelasADetail.objects.filter(pk=key).update(
                        respons = value
                    )
            # Respons F17B
            if ftujuhbelas_b_form.is_valid():
                get_ftujuhbelas_b_id = ResponsFTujuhbelasBDetail.objects.filter(respons_header_id__pk=respons_header.pk).values_list('pk', flat=True)
                data_ftujuhbelas_b = {}
                # Get and Return request to dictionary
                for number, ftujuhbelas_b_id in enumerate(get_ftujuhbelas_b_id, 1):
                    data_ftujuhbelas_b[ftujuhbelas_b_id] = request.POST.get("respons_f17_"+ str(number)+"_b")
                for key, value in data_ftujuhbelas_b.items():
                    fdua = ResponsFTujuhbelasBDetail.objects.filter(pk=key).update(
                        respons = value
                    )            
                
    return render(request, template_name, context)
