from django.shortcuts import render
from django.views.generic import View
from .models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterOpsiRespons,
)


class KuesionerView(View):
    pass
    template_name = 'kuesioner/kuesioner_form_ts.html'
    master_subkuesioner = MasterSubKuesioner.objects.all()
    list_kuesioner = {}
    list_subkuesioner = {}
    context = {
        'list_master_subkuesioner': master_subkuesioner,
    }

    # Import List SubKuesioner 
    subkuesioner_fdua   = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode ='F2')
    subkuesioner_ftiga  = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode ='F3')
    subkuesioner_flima  = subkuesioner_ftiga
    subkuesioner_fenam  = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode ='F6')
    subkuesioner_ftujuh = subkuesioner_fenam
    # Get List Subkuesioner
    context['subkuesioner_fdua']    = subkuesioner_fdua
    context['subkuesioner_ftiga']   = subkuesioner_ftiga
    context['subkuesioner_fenam']   = subkuesioner_fenam
    context['subkuesioner_flima']   = subkuesioner_flima
    context['subkuesioner_ftujuh']  = subkuesioner_ftujuh

    # Import List Opsi Respons
    opsi_respons_fempat = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode ='F4')
    opsi_respons_fdelapan = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode ='F8')
    opsi_respons_fsembilan = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode ='F9')
    opsi_respons_fsepuluh = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode ='F10')

    # HardCode Opsi Respons FDua
    response_options_fdua = {
        ('SB', 'Sangat Besar'),
        ('B', 'Besar'),
        ('CB', 'Cukup Besar'),
        ('K', 'Kurang'),
        ('TSS', 'Tidak Sama Sekali'),
    }
    # Get List Opsi Respons
    context['response_options_fdua'] = response_options_fdua
    context['opsi_respons_fempat'] = opsi_respons_fempat
    context['opsi_respons_fdelapan'] = opsi_respons_fdelapan
    context['opsi_respons_fsembilan'] = opsi_respons_fsembilan

    def get_opsi_respons(self):
        pass


    def get_kuesioner(self):
        master_kuesioner = MasterKuesioner.objects.all()
        # self.list_kuesioner = MasterKuesioner.objects.values_list('kode', 'pertanyaan')
        for kuesioner in master_kuesioner:
                self.list_kuesioner[kuesioner.kode] = kuesioner.pertanyaan
        print(self.list_kuesioner)
        return self.list_kuesioner
        
    def get(self, request):
        self.context['title'] = 'Kuesioner Belmawa'
        self.context['list_kuesioner'] = self.get_kuesioner()
        print(self.get_kuesioner())
        return render(request, self.template_name, self.context)
        
