from django.shortcuts import render, redirect

from django.views.generic import (
    View,    
)

from .models import (
    ResponsHeader,
    ResponsFDuaDetail,
    ResponsFTigaDetail,
    ResponsFEmpatDetail,
    ResponsFLimaDetail,
)

from .forms import (
    ResponsHeaderForm,
    ResponsFDuaForm,
    ResponsFTigaForm,
    ResponsFEmpatForm,
    ResponsFLimaForm,
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


def create(request):  

    # Initialisasi Dictionary
    context = {}
    data = {}

    # Get Kuesioner 
    key_context_kuesioner = 'kuesioner_'
    list_kode_kuesioner = MasterKuesioner.objects.values_list('kode', flat=True)
    for kode in list_kode_kuesioner:
        context[key_context_kuesioner+kode] = MasterKuesioner.objects.filter(kode=kode)
    
    # Respons Form
    header_form     = ResponsHeaderForm(request.POST or None)
    fdua_form       = ResponsFDuaForm(request.POST or None)
    ftiga_form      = ResponsFTigaForm(request.POST or None)
    fempat_form     = ResponsFEmpatForm(request.POST or None)
    flima_form      = ResponsFLimaForm(request.POST or None)

    list_form = [
        ('header_form', header_form),
        ('fdua_form', fdua_form),
        ('ftiga_form', ftiga_form),
        ('fempat_form', fempat_form),
        ('flima_form', flima_form),        
    ]
    for key, value in list_form:
        context[key] = value
    
    # Returns to template
    template_name = 'respons/respons_form.html'
    context['title']        = 'Create Respons'
    # context['header_form']  = header_form
    # context['fdua_form']    = fdua_form
    # context['ftiga_form']   = ftiga_form
    # context['fempat_form']  = fempat_form
    # context['flima_form']   = flima_form
    # ftiga = ResponsFTigaDetail.objects.get('respons')
    # print(ftiga)

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
                    for key, value in list_fdua:
                        data[key] = request.POST.get('respons_' + value)

                    # Save data into database
                    for key, value in data.items():
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
                print(request.POST.getlist('respons_f4'))

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
    return render(request, template_name, context)

