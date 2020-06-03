from django.shortcuts import render
from django.views.generic import View
from .models import (
    MasterKuesioner,
    MasterSubKuesioner,
)


class KuesionerView(View):
    template_name = 'kuesioner/kuesioner_form_ts.html'
    master_subkuesioner = MasterSubKuesioner.objects.all()
    list_kuesioner = {}
    list_subkuesioner = {}
    context = {
        'list_master_subkuesioner': master_subkuesioner,
    }

    # SubKuesioner 
    subkuesioner_fdua = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode ='F2')
    subkuesioner_ftiga = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode ='F3')
    context['subkuesioner_fdua'] = subkuesioner_fdua
    context['subkuesioner_ftiga'] = subkuesioner_ftiga

    # Respons Options FDua
    response_options_fdua = {
        ('SB', 'Sangat Besar'),
        ('B', 'Besar'),
        ('CB', 'Cukup Besar'),
        ('K', 'Kurang'),
        ('TSS', 'Tidak Sama Sekali'),
    }
    context['response_options_fdua'] = response_options_fdua

    def get_kuesioner(self):
        master_kuesioner = MasterKuesioner.objects.all()
        for kuesioner in master_kuesioner:
            self.list_kuesioner[kuesioner.kode] = kuesioner.pertanyaan
        return self.list_kuesioner
        
    def get(self, request):
        self.context['title'] = 'Kuesioner Belmawa'
        self.context['list_kuesioner'] = self.get_kuesioner()
        return render(request, self.template_name, self.context)
        




