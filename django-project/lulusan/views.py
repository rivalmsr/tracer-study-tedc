from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from kuesioner.models import MasterFSatu
from kuesioner.forms import MasterFSatuForm


def create(request):
    print("test masuk sini!")
    form = MasterFSatuForm(request.POST or None)
    template_name = 'lulusan/lulusan_form.html'
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        
        if form.is_valid():
            username = request.POST.get('nama').lower().replace(" ", "_")
            user_password = request.POST.get('nomor_mahasiswa').lower().replace(" ", "_") + request.POST.get('tahun_lulus')
            user_email = request.POST.get('alamat_email')
            if request.method == 'POST':
                user = User.objects.create_user(username, user_email, user_password)
                lulusan_group = Group.objects.get(name='lulusan')
                user.groups.add(lulusan_group)
                user.save()

    context = {
        'title': 'Tambah Data Lulusan',
        'nav_item_lulusan': 'menu-open',
        'nav_status_lulusan': 'active',
        'nav_status_tambah_lulusan': 'active',
        'form': form,
    }

    return render(request, template_name, context)


# class LulusanCreateView(CreateView):
#     form_class  = MasterFSatuForm
#     template_name = 'lulusan/lulusan_form.html'
#     extra_context = {

#         'title':'Tambah Data Mahasiswa'
#     }

#     def get_context_data(self, *args, **kwargs):
#         kwargs.update(self.extra_context)
#         return super().get_context_data(*args, **kwargs)


class LulusanListView(ListView):
    model               = MasterFSatu
    context_object_name = 'list_of_lulusan'
    template_name       = 'lulusan/lulusan_list.html'
    extra_context       = {
        'title': 'Daftar Lulusan',
        'nav_item_lulusan': 'menu-open',
        'nav_status_lulusan': 'active',
        'nav_status_daftar_lulusan': 'active',
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class LulusanDetailView(DetailView):
    model               = MasterFSatu
    context_object_name = 'lulusan'
    template_name       = 'lulusan/lulusan_detail.html'
    extra_context       = {
        'title': 'Detail Lulusan',
        'nav_item_lulusan': 'menu-open',
        'nav_status_lulusan': 'active',
        'nav_status_daftar_lulusan': 'active',
    }


class LulusanUpdateView(UpdateView):
    model               = MasterFSatu
    form_class          = MasterFSatuForm
    template_name       = 'lulusan/lulusan_form.html'
    success_url         = reverse_lazy('lulusan:list')
    extra_context       = {
        'title': 'Edit Data Mahasiswa',
        'nav_item_lulusan': 'menu-open',
        'nav_status_lulusan': 'active',
        'nav_status_daftar_lulusan': 'active',
    }

def delete(request, delete_id):
    template_name = 'lulusan/lulusan_confirm_delete.html'
    lulusan = MasterFSatu.objects.get(pk=delete_id)
    context = {
        'title': 'Hapus Data Mahasiswa',
        'lulusan': lulusan
    }

    # get lulusan form database 
    lulusan_account = get_object_or_404(MasterFSatu, id = delete_id)
    # get user by lulusan from database
    lulusan_group = get_object_or_404(User, email=lulusan_account.alamat_email)

    if request.method == 'POST':
        # delete lulusan
        lulusan_account.delete()
        # delete user
        lulusan_group.delete()
        return redirect('lulusan:list')

    return render(request, template_name, context)

# class LulusanDeleteView(DeleteView):
#     model               = MasterFSatu
#     content_object_name = 'lulusan'
#     template_name       = 'lulusan/lulusan_confirm_delete.html'
#     success_url         = reverse_lazy('lulusan:list')

def lulusan_profile(request):
    template_name = 'lulusan/lulusan_profile.html'
    context = {
        'title': 'Profil Lulusan'
    }

    return render(request, template_name, context)