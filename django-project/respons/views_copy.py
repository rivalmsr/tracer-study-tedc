import xlwt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

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
        'title': 'List Responden',
        'nav_item_responden': 'menu-open',
        'nav_status_responden': 'active',
        'nav_status_daftar_responden': 'active',
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

def detail(request, detail_id):
    context = {}
    template_name = 'respons/respons_detail.html'

    # get data F2-F8 from database
    data_respons_header = ResponsHeader.objects.get(pk=detail_id)
    data_fdua = ResponsFDuaDetail.objects.filter(respons_header_id=data_respons_header.pk)
    data_ftiga = ResponsFTigaDetail.objects.get(respons_header_id=data_respons_header.pk)
    get_data_fempat = ResponsFEmpatDetail.objects.values_list('respons', flat=True).get(respons_header_id=data_respons_header.pk)
    data_fempat = get_data_fempat.split(";")
    data_flima = ResponsFLimaDetail.objects.get(respons_header_id=data_respons_header.pk)
    data_fenam = ResponsFEnamDetail.objects.get(respons_header_id=data_respons_header.pk)
    data_ftujuh = ResponsFTujuhDetail.objects.get(respons_header_id=data_respons_header.pk)
    data_ftujuh_a = ResponsFTujuhADetail.objects.get(respons_header_id=data_respons_header.pk)
    data_fdelapan = ResponsFDelapanDetail.objects.get(respons_header_id=data_respons_header.pk)
    # get data F17 from database
    data_ftujuhbelas_a = ResponsFTujuhbelasADetail.objects.filter(respons_header_id=data_respons_header.pk)
    data_ftujuhbelas_b = ResponsFTujuhbelasBDetail.objects.filter(respons_header_id=data_respons_header.pk)
    # return data F2-F8 and F17 into context
    context = {
        'title': 'Detail Respons',
        'nav_item_responden': 'menu-open',
        'nav_status_responden': 'active',
        'nav_status_daftar_responden': 'active',
        'data_respons_header': data_respons_header,
        'data_fdua': data_fdua,
        'data_ftiga': data_ftiga,
        'data_fempat': data_fempat,
        'data_flima': data_flima,
        'data_fenam': data_fenam,
        'data_ftujuh': data_ftujuh,
        'data_ftujuh_a': data_ftujuh_a,
        'data_fdelapan': data_fdelapan,
        'data_ftujuhbelas_a': data_ftujuhbelas_a,
        'data_ftujuhbelas_b': data_ftujuhbelas_b,
    }
    # check condition if value is F8-02
    get_F8_value = MasterOpsiRespons.objects.get(kode='F8-02')
    context['get_F8_value'] = get_F8_value
    if data_fdelapan.respons == get_F8_value.opsi_respons:
        # get data F9 and F10 from database
        get_data_fsembilan = ResponsFSembilanDetail.objects.values_list('respons', flat=True).get(respons_header_id=data_respons_header.pk)
        data_fsembilan = get_data_fsembilan.split(";")
        data_fsepuluh = ResponsFSepuluhDetail.objects.get(respons_header_id=data_respons_header.pk)
        # return data F9 and F10 into context
        context['data_fsembilan'] = data_fsembilan
        context['data_fsepuluh'] = data_fsepuluh
    else :
        # get data F11-F16 from database
        data_fsebelas = ResponsFSebelasDetail.objects.get(respons_header_id=data_respons_header.pk)
        data_ftigabelas = ResponsFTigabelasDetail.objects.filter(respons_header_id=data_respons_header.pk)
        data_fempatbelas = ResponsFEmpatbelasDetail.objects.get(respons_header_id=data_respons_header.pk)
        data_flimabelas = ResponsFLimabelasDetail.objects.get(respons_header_id=data_respons_header.pk)
        get_data_fenambelas = ResponsFEnambelasDetail.objects.values_list('respons', flat=True).get(respons_header_id=data_respons_header.pk)
        data_fenambelas = get_data_fenambelas.split(";")
        # return data F11-F16 into context
        context['data_fsebelas'] = data_fsebelas
        context['data_ftigabelas'] = data_ftigabelas
        context['data_fempatbelas'] = data_fempatbelas
        context['data_flimabelas'] = data_flimabelas
        context['data_fenambelas'] = data_fenambelas
    
    # get data kuesioner form database
    key_context_kuesioner = 'kuesioner_'
    list_kode_kuesioner = MasterKuesioner.objects.values_list('kode', flat=True)
    # return data kuesioner into context
    for kode in list_kode_kuesioner:
        context[key_context_kuesioner+kode] = MasterKuesioner.objects.filter(kode=kode)
    
    return render(request, template_name, context)

def create_with_ajax(request):
    if request.method == 'POST':
        print(request.POST['getrow'])


def create(request):  
    # Initialisasi Dictionary 
    context = {}
    
    # Returns to template
    template_name       = 'respons/respons_form.html'
    context = {
        'title': 'Create Respons',
        'nav_item_kuesioner': 'menu-open',
        'nav_status_kuesioner': 'active',
        'nav_status_pengisian_kuesioner': 'active',
    }

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
                get_respons_header = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1'))
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
                get_list_respons_f3_1 = request.POST.getlist('respons_f3_1')
                get_respons_f3_1 = 0

                for value in get_list_respons_f3_1:
                    if value != "":
                        get_respons_f3_1 = value

                if ftiga_form.is_valid():
                    ftiga = ResponsFTigaDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f3')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = get_respons_f3_1,
                        keterangan              = request.POST.get('respons_f3_2')
                    )
                    ftiga.save()

                # Respons F4
                if fempat_form.is_valid():
                    data_fempat = ""
                    getlist_fempat = request.POST.getlist('respons_f4')
                     
                    for value in getlist_fempat:
                        data_fempat += value + ";" 

                    fempat = ResponsFEmpatDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f4')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = data_fempat
                    )
                    fempat.save()
                    
                # Respons F5
                get_list_respons_f5_1 = request.POST.getlist('respons_f5_1')
                get_respons_f5_1 = 0

                for value in get_list_respons_f5_1:
                    if value != "":
                        get_respons_f5_1 = value

                if flima_form.is_valid():
                    flima = ResponsFLimaDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f5')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = get_respons_f5_1,
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
                        data_fsembilan = ""
                        getlist_respons_f9 = request.POST.getlist('respons_f9')
                         
                        for value in getlist_respons_f9:
                            data_fsembilan += value + ";"

                        fsembilan = ResponsFSembilanDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f9')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = data_fsembilan
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
                        data_fenambelas = ""
                        getlist_respons_fenambelas = request.POST.getlist('respons_f16')

                        for value in getlist_respons_fenambelas:
                            data_fenambelas += value + ";"

                        fenambelas = ResponsFEnambelasDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f16')),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = data_fenambelas
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

                return redirect('respons:detail', get_respons_header.pk)

    return render(request, template_name, context)

def update(request, update_id):
    template_name       = 'respons/respons_form.html'
    context             = {
        'title': 'Create Respons',
        'nav_item_responden': 'menu-open',
        'nav_status_responden': 'active',
        'nav_status_daftar_responden': 'active',
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
    data_update_fempat = get_value_fempat.respons.split(";")
    data_form_fempat = {
        'respons_f4': data_update_fempat
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
        data_update_fsembilan = get_value_fsembilan.respons.split(";")
        data_form_fsembilan = {
            'respons_f9': data_update_fsembilan
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
        data_update_fenambelas = get_value_fenambelas.respons.split(";")
        data_form_fenambelas = {
            'respons_f16': data_update_fenambelas
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
            get_list_respons_f3_1 = request.POST.getlist('respons_f3_1')
            get_respons_f3_1 = 0

            for value in get_list_respons_f3_1:
                if value != "":
                    get_respons_f3_1 = value

            if ftiga_form.is_valid():
                get_ftiga = ResponsFTigaDetail.objects.get(respons_header_id__pk=respons_header.pk)
                ftiga = ResponsFTigaDetail.objects.filter(pk=get_ftiga.pk).update(
                    respons = get_respons_f3_1,
                    keterangan = request.POST.get('respons_f3_2')
                )
            # Respons F4
            if fempat_form.is_valid():
                data_fempat = ""
                getlist_respons_f4 = request.POST.getlist('respons_f4')

                # return value into variable
                for value in getlist_respons_f4:
                     data_fempat += value + ";"   

                # return value getlist into database
                get_fempat = ResponsFEmpatDetail.objects.get(respons_header_id__pk=respons_header.pk)
                fempat = ResponsFEmpatDetail.objects.filter(pk=get_fempat.pk).update(
                    respons = data_fempat
                )

            # Respons F5
            get_list_respons_f5_1 = request.POST.getlist('respons_f5_1')
            get_respons_f5_1 = 0

            for value in get_list_respons_f5_1:
                if value != "":
                    get_respons_f5_1 = value

            if flima_form.is_valid():
                get_flima = ResponsFLimaDetail.objects.get(respons_header_id__pk=respons_header.pk)
                flima = ResponsFLimaDetail.objects.filter(pk=get_flima.pk).update(
                    respons = get_respons_f5_1,
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
                    data_fsembilan = ""
                    getlist_respons_f9 = request.POST.getlist('respons_f9')

                    # return value into variable
                    for value in getlist_respons_f9:
                        data_fsembilan += value + ";"

                    # return data into database 
                    get_fsembilan = ResponsFSembilanDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fsembilan = ResponsFSembilanDetail.objects.filter(pk=get_fsembilan.pk).update(
                        respons = data_fsembilan
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
                    data_fenambelas = ""
                    getlist_respons_f16 = request.POST.getlist('respons_f16')
                    # return value into variable
                    for value in getlist_respons_f16:
                        data_fenambelas += value + ";"
                    get_fenambelas = ResponsFEnambelasDetail.objects.get(respons_header_id__pk=respons_header.pk)
                    fenambelas = ResponsFEnambelasDetail.objects.filter(pk=get_fenambelas.pk).update(
                        respons = data_fenambelas
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
            return redirect('respons:detail', update_id)
                
    return render(request, template_name, context)

def export_xls(request):
    response = HttpResponse(content_type="")
    response['Content-Disposition'] = 'attachment; filename="Master-Kuesioner.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Kuesioner')

    # sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    

    columns = [
        'kdptimsmh', 'kdpstmsmh', 'nimhsmsmh', 'nmmhsmsmh', 'telpomsmh', 'emailmsmh', 'tahun_lulus', #fsatu
        'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', #fdua
        'f301', 'f302', 'f303', #ftiga
        'f401', 'f402', 'f403', 'f404', 'f405', 'f406', 'f407', 'f408', 'f409', 'f410', 'f411', 'f412', 'f413', 'f414', 'f415', 'f416', #fempat
        'f6', #fenam
        'f501', 'f502', 'f503', #flima
        'f7', #ftujuh
        'f7a', #ftuju_a
        'f8', #fdelapan
        'f901', 'f902', 'f903', 'f904', 'f905', 'f906', #fsembilan
        'f101', 'f102', #fsepuluh
        'f1101', 'f1102', #fsebelas
        'f1201', 'f1202', #fduabelas
        'f1301', 'f1302', 'f1303', #ftigabelas
        'f14', #fempatbelas
        'f15', #fempatbelas
        'f1601', 'f1602', 'f1603', 'f1604', 'f1605', 'f1606', 'f1607', 'f1608', 'f1609', 'f1610', 'f1611', 'f1612', 'f1613', 'f1614', #fempatbelas
        'f1701', 'f1702b', 'f1703',	'f1704b', 'f1705', 'f1705a', 'f1706', 'f1706ba', 'f1707', 'f1708b', 'f1709', 'f1710b', 
        'f1711', 'f1711a', 'f1712b', 'f1712a', 'f1713', 'f1714b', 'f1715', 'f1716b', 'f1717', 'f1718b', 'f1719', 'f1720b', 
        'f1721', 'f1722b', 'f1723', 'f1724b', 'f1725', 'f1726b', 'f1727', 'f1728b', 'f1729', 'f1730b', 
        'f1731', 'f1732b', 'f1733', 'f1734b', 	'f1735', 'f1736b', 'f1737', 'f1737a', 'f1738', 'f1738ba', 'f1739', 'f1740b', 
        'f1741', 'f1742b', 'f1743', 'f1744b', 'f1745', 'f1746b', 'f1747', 'f1748b', 'f1749', 'f1750b', 'f1751', 'f1752b', 'f1753', 'f1754b', #ftujubelas_a and ftujubelas_b

    ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # empty list master_rows
    master_rows = []
    # sheet body, remaining rows
    print("start test")
    list_header_respons_id = ResponsHeader.objects.all().values_list('master_fsatu_id__pk', flat=True).order_by('pk')
    for master_fsatu_id in list_header_respons_id:
        # empty list temp_rows
        temp_rows = []
        # get respons_header form database
        get_respons_header = ResponsHeader.objects.get(master_fsatu_id__pk=master_fsatu_id)

        # insert values fsatu into temp_rows
        fsatu_rows = MasterFSatu.objects.values_list('master_poltek_id__kode', 'master_prodi_id__kode', 'nomor_mahasiswa', 'nama', 'nomor_telepon', 'alamat_email', 'tahun_lulus').get(pk=master_fsatu_id)
        for row in fsatu_rows:
            temp_rows.append(row)

        # insert values fdua into temp_rows
        fdua_rows = ResponsFDuaDetail.objects.filter(respons_header_id__pk=get_respons_header.id).values_list('respons', flat=True).order_by('id')
        temp_rows.extend(fdua_rows)

        # insert values ftiga into temp_rows 
        ftiga_rows = ResponsFTigaDetail.objects.get(respons_header_id__pk=get_respons_header.id)
        list_ftiga = []
        if ftiga_rows.keterangan == 'Saya tidak mencari kerja':
            list_ftiga = [ftiga_rows.keterangan, '', '']
        elif ftiga_rows.keterangan == 'Sebelum Lulus':
            list_ftiga = [ftiga_rows.respons, ftiga_rows.keterangan, '']
        elif ftiga_rows.keterangan == 'Sesudah Lulus':
            list_ftiga = [ftiga_rows.respons, '', ftiga_rows.keterangan]
        temp_rows.extend(list_ftiga)

        # insert values fempat into temp_rows 
        # initialization
        list_kode_and_respons = {}
        list_kode = []
        list_fempat = []
        # get values fempat and insert to list
        get_value_fempat = ResponsFEmpatDetail.objects.get(respons_header_id__pk=get_respons_header.id)
        list_respons_fempat = get_value_fempat.respons.split(';')
        for respons in list_respons_fempat:
            if respons != '':
                if respons == 'Lainnya':
                    get_opsi_respons = MasterOpsiRespons.objects.get(kode='F4-15')
                else:
                    get_opsi_respons = MasterOpsiRespons.objects.get(opsi_respons=respons)
            list_kode_and_respons[get_opsi_respons.kode] = get_opsi_respons.opsi_respons
            list_kode.append(get_opsi_respons.kode)
        # list kode fempat
        list_queueing_fempat = [
            'F4-01', 'F4-02', 'F4-03', 'F4-04', 'F4-05', 'F4-06', 
            'F4-07', 'F4-08', 'F4-09',  'F4-10', 'F4-11', 'F4-12',
             'F4-13', 'F4-14', 'F4-15', 'F4-16',  
        ]
        # make list fempat such as queuing
        for queue in list_queueing_fempat:
            if queue in list_kode:
                get_value = list_kode_and_respons.get(queue)
                list_fempat.append(get_value)
            else:
                list_fempat.append('')
        temp_rows.extend(list_fempat)

        # insert values fenam into temp_rows 
        get_value_fenam = ResponsFEnamDetail.objects.get(respons_header_id__pk=get_respons_header.id)
        temp_rows.extend(str(get_value_fenam.respons))

        # insert values flima into temp_rows
        get_value_flima = ResponsFLimaDetail.objects.get(respons_header_id__pk=get_respons_header.id)
        checking_value = [get_value_flima.respons, get_value_flima.keterangan]
        temp_flima = []
        if get_value_flima.keterangan == 'Sebelum Lulus':
            temp_flima = [get_value_flima.respons, get_value_flima.keterangan, '']
        else:
            temp_flima = [get_value_flima.respons, '', get_value_flima.keterangan]
        temp_rows.extend(temp_flima)

        # insert values ftujuh into temp_rows
        get_value_ftujuh = ResponsFTujuhDetail.objects.get(respons_header_id__pk=get_respons_header.id)
        temp_ftujuh = get_value_ftujuh.respons
        temp_rows.append(str(temp_ftujuh))

        # insert values ftujuh_a into temp_rows
        get_value_ftujuh_a = ResponsFTujuhADetail.objects.get(respons_header_id__pk=get_respons_header.id)
        temp_ftujuh_a = get_value_ftujuh_a.respons
        temp_rows.append(str(temp_ftujuh_a))

        # insert values fdelapan into temp_rows
        get_value_fdelapan = ResponsFDelapanDetail.objects.get(respons_header_id__pk=get_respons_header.id)
        temp_fdelapan = get_value_fdelapan.respons
        temp_rows.append(temp_fdelapan)

        # Optional Conditions F9 - F10
        if ResponsFSembilanDetail.objects.filter(respons_header_id__pk=get_respons_header.id):

            # insert values fsembilan into temp_rows
            # initialization list
            list_kode_and_respons = {}
            list_kode = []
            list_fsembilan = []
            get_value_fsembilan = ResponsFSembilanDetail.objects.get(respons_header_id__pk=get_respons_header.id)
            list_respons_fsembilan = get_value_fsembilan.respons.split(';')
            for respons in list_respons_fsembilan:
                if respons != '':
                    if respons == 'Lainnya':
                        get_opsi_respons = MasterOpsiRespons.objects.get(kode='F9-05')
                    else:
                        get_opsi_respons = MasterOpsiRespons.objects.get(opsi_respons=respons)
                list_kode_and_respons[get_opsi_respons.kode] = get_opsi_respons.opsi_respons
                list_kode.append(get_opsi_respons.kode)

            list_queuing_fsembilan = [
                'F9-01', 'F9-02', 'F9-03', 'F9-04', 'F9-05', 'F9-06' 
            ]
            # make list fempat such as queuing
            for queue in list_queuing_fsembilan:
                if queue in list_kode:
                    get_value = list_kode_and_respons.get(queue)
                    list_fsembilan.append(get_value)
                else:
                    list_fsembilan.append('')
            temp_rows.extend(list_fsembilan)

            # insert values fsepuluh into temp_rows
            get_value_fsepuluh = ResponsFSepuluhDetail.objects.get(respons_header_id__pk=get_respons_header.id)
            temp_fsepuluh = [get_value_fsepuluh.respons, '']
            temp_rows.extend(temp_fsepuluh)

            # IF NOT VALUES IN RESPONS F11 - F16 TO INSERT ROWS
            list_fsebelas = ['', '']
            list_fduabelas = ['', '']
            list_ftigabelas = ['', '', '']
            list_fempatbelas = ['']
            list_flimabelas = ['']
            list_fenambelas = ['', '', '', '', '', '', '','', '', '', '', '', '', '', ]
            temp_rows.extend(list_fsebelas)
            temp_rows.extend(list_fduabelas)
            temp_rows.extend(list_ftigabelas)
            temp_rows.extend(list_fempatbelas)
            temp_rows.extend(list_flimabelas)
            temp_rows.extend(list_fenambelas)
        else:
            # IF NOT VALUES IN RESPONS F9 - F10 TO INSERT ROWS
            list_fsembilan = ['', '', '', '', '', '' ]
            list_fsepuluh = ['', '']
            temp_rows.extend(list_fsembilan)
            temp_rows.extend(list_fsepuluh)

            # insert values fsebelas into temp_rows
            get_value_fsebelas = ResponsFSebelasDetail.objects.get(respons_header_id__pk=get_respons_header.id)
            temp_fsebelas = [get_value_fsebelas.respons, '']
            temp_rows.extend(temp_fsebelas)

            # IF NOT VALUES IN RESPONS F12 TO INSERT ROWS
            list_fduabelas = ['', '']
            temp_rows.extend(list_fduabelas)

            # insert values ftigabelas into temp_rows
            # initialization list
            temp_ftigabelas = []
            get_values_ftigabelas = ResponsFTigabelasDetail.objects.filter(respons_header_id__pk=get_respons_header.id).values_list('respons', flat=True).order_by('pk')
            for value in get_values_ftigabelas:
                temp_ftigabelas.append(value)
            temp_rows.extend(temp_ftigabelas)

            # insert values fempat into temp_rows
            get_values_fempatbelas = ResponsFEmpatbelasDetail.objects.get(respons_header_id__pk=get_respons_header.id)
            temp_fempatbelas = get_values_fempatbelas.respons
            temp_rows.append(temp_fempatbelas)

            # insert values flimabelas into temp_rows
            get_values_flimabelas = ResponsFLimabelasDetail.objects.get(respons_header_id__pk=get_respons_header.id)
            temp_flimabelas = get_values_flimabelas.respons
            temp_rows.append(temp_flimabelas)

            # insert values fenambelas into temp_rows
            # initialization
            list_fenambelas = []
            list_kode_and_respons = {}
            list_kode = []
            get_values_fenambelas = ResponsFEnambelasDetail.objects.get(respons_header_id__pk=get_respons_header.id)
            list_values = get_values_fenambelas.respons.split(';')
            print('list values:', list_values)
            for value in list_values:
                if value != '':
                    if value == 'Lainnya':
                        get_opsi_respons = MasterOpsiRespons.objects.get(kode='F16-13')
                    else:
                        get_opsi_respons = MasterOpsiRespons.objects.get(opsi_respons=value)
                list_kode_and_respons[get_opsi_respons.kode] = get_opsi_respons.opsi_respons
                list_kode.append(get_opsi_respons.kode)
            # queuing concept
            list_queuing_fenambelas = [
                'F16-01', 'F16-02', 'F16-03', 'F16-04', 'F16-05', 'F16-06', 'F16-07', 
                'F16-08', 'F16-09', 'F16-10', 'F16-11', 'F16-12', 'F16-13', 'F16-14', 
            ]

            for queue in list_queuing_fenambelas:
                if queue in list_kode:
                    get_value = list_kode_and_respons.get(queue)
                    list_fenambelas.append(get_value)
                else:
                    list_fenambelas.append('')

            print('list_fenambelas', list_fenambelas)
            temp_rows.extend(list_fenambelas)
        # insert values ftujuhbelas into temp_rows
        # initializition
        list_ftujuhbelas = []
        get_values_ftujuhbelas_a = ResponsFTujuhbelasADetail.objects.filter(respons_header_id__pk=get_respons_header.id).values_list('respons', flat=True).order_by('pk')
        get_values_ftujuhbelas_b = ResponsFTujuhbelasBDetail.objects.filter(respons_header_id__pk=get_respons_header.id).values_list('respons', flat=True).order_by('pk')
        for value_a, value_b in zip(get_values_ftujuhbelas_a, get_values_ftujuhbelas_b):
            list_ftujuhbelas.append(value_a)
            list_ftujuhbelas.append(value_b)
        temp_rows.extend(list_ftujuhbelas)
        # result all values to master rows
        master_rows.append(temp_rows)

    for row in master_rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response

def unduh_data(request):
    template_name   = 'respons/unduh_data_tracer.html'
    context = {
        'title': 'Unduh Data Tracer',
        'nav_item_responden': 'menu-open',
        'nav_status_responden': 'active',
        'nav_status_unduh_data_responden': 'active',
    }

    return render(request, template_name, context)