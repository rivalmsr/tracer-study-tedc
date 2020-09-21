from django.shortcuts import render
from django.views.generic import (
     TemplateView,
     ListView,
     View,
     DetailView,
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

class KuesionerDetailView(DetailView):
    pass

class KuesionerListView(ListView):
    model = MasterKuesioner
    context_object_name = 'list_of_kuesioner'
    template_name = 'kuesioner/kuesioner_list.html'    
    extra_context = {
        'title' : 'List Kuesioner',
        'nav_item_kuesioner': 'menu-open',
        'nav_status_kuesioner': 'active',
        'nav_status_daftar_kuesioner': 'active',
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
    

        
