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
    ftujuhbelas_b_form  = ResponsFTujuhbelasAForm(request.POST or None)
    

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
    print(request.POST)
    # Reqeust Method Check
    if request.method == 'POST':
        if header_form.is_valid:
            fsatu = ResponsHeader.objects.create( 
                master_fsatu_id = MasterFSatu.objects.get(pk=request.POST.get('respons_f1')) 
            )
            fsatu.save()
            
            if  ResponsHeader.objects.filter(master_fsatu_id__pk=request.POST.get('respons_f1')).exists():
                # Respons F2
                if fdua_form.is_valid:
                    # Get Request 
                    list_fdua = [
                        ('F2-1', 'f21'), 
                        ('F2-2', 'f22'), 
                        ('F2-3', 'f23'), 
                        ('F2-4', 'f24'), 
                        ('F2-5', 'f25'), 
                        ('F2-6', 'f26'), 
                        ('F2-7', 'f27')
                    ]
                    data_fdua = {}
                    for key, value in list_fdua:
                        data_fdua[key] = request.POST.get('respons_' + value)

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
                if ftiga_form.is_valid:
                    ftiga = ResponsFTigaDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f3')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f31'),
                        keterangan              = request.POST.get('respons_f32')
                    )
                    ftiga.save()

                # Respons F4
                if fempat_form.is_valid:
                    fempat = ResponsFEmpatDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f4')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.getlist('respons_f4')
                    )
                    ftiga.save()

                # Respons F5
                if flima_form.is_valid:
                    flima = ResponsFLimaDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f5')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f51'),
                        keterangan              = request.POST.get('respons_f52')
                    )
                    flima.save()

                # Respons F6
                if fenam_form.is_valid:
                    fenam = ResponsFEnamDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f6')),
                        master_subkuesioner_id  = MasterSubKuesioner.objects.get(master_kuesioner_id__pk=request.POST.get('kuesioner_f6')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f6'),
                    )
                    fenam.save()

                # Respons F7
                if ftujuh_form.is_valid:
                    ftujuh = ResponsFTujuhDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f7')),
                        master_subkuesioner_id  = MasterSubKuesioner.objects.get(master_kuesioner_id__pk=request.POST.get('kuesioner_f7')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f7'),
                    )
                    ftujuh.save()

                # Respons F7A
                if ftujuh_a_form.is_valid:
                    ftujuh_a = ResponsFTujuhADetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f7A')),
                        master_subkuesioner_id  = MasterSubKuesioner.objects.get(master_kuesioner_id__pk=request.POST.get('kuesioner_   f7A')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f7A'),
                    )
                    ftujuh_a.save()
                
                # Respons F8
                if fdelapan_form.is_valid:
                    fdelapan = ResponsFDelapanDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f8')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f8'),
                    )
                    fdelapan.save()
                
                # Respons F9
                if fsembilan_form.is_valid:
                    fsembilan = ResponsFSembilanDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f9')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.getlist('respons_f9'),
                    )
                    fsembilan.save()

                # Respons F10
                if fsepuluh_form.is_valid:
                    fsepuluh = ResponsFSepuluhDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f10')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f10'),
                    )
                    fsepuluh.save()
                
                # Respons F11
                if fsebelas_form.is_valid:
                    fsebelas = ResponsFSebelasDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f11')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f11'),
                    )
                    fsebelas.save()

                # Respons F13
                if ftigabelas_form.is_valid:
                    list_ftigabelas = [
                        ('F13-1', 'f131'),
                        ('F13-2', 'f132'),
                        ('F13-3', 'f133'),
                    ]
                    data_ftigabelas = {}
                    for key, value in list_ftigabelas:
                        data_ftigabelas[key] = request.POST.get('respons_'+value)

                    for key, value in data_ftigabelas.items():
                        ftigabelas = ResponsFTigabelasDetail.objects.create(
                            master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f13')),
                            master_subkuesioner_id  = MasterSubKuesioner.objects.get(kode=key),
                            respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                            respons                 = value
                        )
                        ftigabelas.save()

                # Respons F14
                if fempatbelas_form.is_valid:
                    fempatbelas = ResponsFEmpatbelasDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f14')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f14'),
                    )
                    fempatbelas.save()

                # Respons F15
                if flimabelas_form.is_valid:
                    flimabelas = ResponsFLimabelasDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f15')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.get('respons_f15'),
                    )
                    flimabelas.save()

                # Respons F16
                if fenambelas_form.is_valid:
                    fenambelas = ResponsFEnambelasDetail.objects.create(
                        master_kuesioner_id     = MasterKuesioner.objects.get(pk=request.POST.get('kuesioner_f16')),
                        respons_header_id       = ResponsHeader.objects.get(master_fsatu_id__pk=request.POST.get('respons_f1')),
                        respons                 = request.POST.getlist('respons_f16'),
                    )
                    fenambelas.save()

                # Respons F17A
                if ftujuhbelas_a_form.is_valid:
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
                if ftujuhbelas_b_form.is_valid:
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

