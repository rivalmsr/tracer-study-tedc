from django.shortcuts import render
from django.views.generic import (
     TemplateView,
     View,
)
from .models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterOpsiRespons,
)

class KuesionerIndex(TemplateView):
    template_name = 'kuesioner/index.html'
    context = {}

    def get_context_data(self, *args, **kwargs):
        self.context['title'] = 'Home Kuesioner'
        return self.context

class KuesionerForm(TemplateView):
    template_name = 'kuesioner/kuesioner_form_ts.html'
    list_kuesioner = {}
    list_subkuesioner = {}
    context = {}

    def get_subkuesioner(self):
        list_subkuesioner = (
            'F2','F3','F5','F6', 'F7','F7A', 'F13', 'F17A', 'F17B'
            )
        key_context = 'subkuesioner_'
        for kode in list_subkuesioner:
            self.context[key_context+kode] = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode=kode)
        return self.context

    def get_kuesioner(self):
        key_context_kuesioner = 'kuesioner_'
        list_kode_kuesioner = MasterKuesioner.objects.values_list('kode', flat=True)
        for kode in list_kode_kuesioner:
            self.context[key_context_kuesioner+kode] = MasterKuesioner.objects.filter(kode=kode)
        return self.context

    def get_opsi_respons(self):
        list_kuesioner_respons = (
            'F2','F4', 'F8', 'F9', 'F10', 'F11', 'F13', 'F14', 'F15', 'F16', 'F17A', 'F17B'
            )
        key_context = 'opsi_respons_'
        for kode in list_kuesioner_respons:
            self.context[key_context+kode] = MasterOpsiRespons.objects.filter(master_kuesioner_id__kode=kode)
        return self.context

    def get_context_data(self, *args, **kwargs):
        self.context['title'] = 'Kuesioner Belmawa'
        self.get_subkuesioner()
        self.get_kuesioner()
        self.get_opsi_respons()
        return self.context


class KuesionerView(View):
    template_name = 'kuesioner/kuesioner_form_ts.html'    
    context = {}

    def post(self, *args, **kwargs):
        pass    

    def get(self, *args, **kwargs):
        pass

        
