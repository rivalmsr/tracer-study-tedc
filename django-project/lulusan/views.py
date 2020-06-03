from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from kuesioner.models import MasterFSatu
from kuesioner.forms import MasterFSatuForm

class LulusanCreateView(CreateView):
    form_class  = MasterFSatuForm
    template_name = 'lulusan/lulusan_form.html'
    extra_context = {

        'title':'Tambah Data Mahasiswa'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class LulusanListView(ListView):
    model               = MasterFSatu
    context_object_name = 'list_of_lulusan'
    template_name       = 'lulusan/lulusan_list.html'
    extra_context       = {
        'page_title': 'List Lulusan'
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class LulusanDetailView(DetailView):
    model               = MasterFSatu
    context_object_name = 'lulusan'
    template_name       = 'lulusan/lulusan_detail.html'


class LulusanUpdateView(UpdateView):
    model               = MasterFSatu
    form_class          = MasterFSatuForm
    template_name       = 'lulusan/lulusan_form.html'
    success_url         = reverse_lazy('lulusan:list')
    extra_context       = {
        'title': 'Edit Data Mahasiswa'
    }


class LulusanDeleteView(DeleteView):
    model               = MasterFSatu
    content_object_name = 'lulusan'
    template_name       = 'lulusan/lulusan_confirm_delete.html'
    success_url         = reverse_lazy('lulusan:list')