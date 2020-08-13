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
# Email System 
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from kuesioner.models import MasterFSatu
from kuesioner.forms import MasterFSatuForm
from .models import BiodataLulusan
from django.views.generic import TemplateView
from .forms import BiodataLulusanForm

class Index(TemplateView):
    template_name= "lulusan/lulusan_activation_account.html"

def mail_system(param_mail_subject, param_template_name, param_context_mail, param_user_mail ):
    # MAIL SYSTEM
    htmly = get_template(param_template_name)
    subject, form_mail, to = param_mail_subject, 'rivalmusripal@gmail.com', param_user_mail
    html_content = htmly.render(param_context_mail)
    msg = EmailMultiAlternatives(subject, html_content, form_mail, [to])
    msg.attach_alternative(html_content, "text/html")
    return msg.send()


def create(request):
    form = MasterFSatuForm(request.POST or None)
    template_name = 'lulusan/lulusan_form.html'
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
        if MasterFSatu.objects.filter(nomor_mahasiswa=request.POST.get('nomor_mahasiswa')).exists():
            biodata_lulusan = BiodataLulusan.objects.create(
                master_fsatu_id = MasterFSatu.objects.get(nomor_mahasiswa=request.POST.get('nomor_mahasiswa'))
            )
            biodata_lulusan.save()

        if form.is_valid():
            username = request.POST.get('nama').lower().replace(" ", "_")
            user_password = request.POST.get('nomor_mahasiswa').lower().replace(" ", "_") + request.POST.get('tahun_lulus')
            user_email = request.POST.get('alamat_email')
            if request.method == 'POST':
                user = User.objects.create_user(username, user_email, user_password)
                user.is_active = False
                # add user to group lulusan
                lulusan_group = Group.objects.get(name='lulusan')
                user.groups.add(lulusan_group)
                user.save()

                # MAIL SYSTEM
                current_site = get_current_site(request)
                mail_subject = 'Aktifasi Akun Tracer Study Anda'
                mail_template_name = 'lulusan/lulusan_activation_account.html'
                mail_context = {
                    'username': username,
                    'user_password': user_password,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
                send_email = mail_system(param_mail_subject=mail_subject, param_template_name=mail_template_name, param_context_mail=mail_context, param_user_mail=user_email)

    context = {
        'title': 'Tambah Data Lulusan',
        'nav_item_lulusan': 'menu-open',
        'nav_status_lulusan': 'active',
        'nav_status_tambah_lulusan': 'active',
        'form': form,
    }

    return render(request, template_name, context)



def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExists):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpReesponse('Activation link is invalid!')


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


class LulusanProfileView(DetailView):
    model               = MasterFSatu
    context_object_name = 'lulusan'
    template_name       = 'lulusan/lulusan_profile.html'
    extra_context       = {
        'title': 'Detail Lulusan',
        'nav_item_lulusan': 'menu-open',
        'nav_status_lulusan': 'active',
        'nav_status_daftar_lulusan': 'active',
    }

    def get_context_data(self, *args, **kwargs):
        # get biodata by slug
        slug = self.kwargs.get('slug')
        biodata_lulusan = BiodataLulusan.objects.get(master_fsatu_id__slug=slug)
        self.extra_context['biodata_lulusan'] = biodata_lulusan
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
    

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


class LulusanUpdateBiodataView(UpdateView):
    model               = BiodataLulusan
    form_class          = BiodataLulusanForm
    template_name       = 'lulusan/lulusan_profile_form.html'
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


def lulusan_profile(request):
    template_name = 'lulusan/lulusan_profile.html'
    context = {
        'title': 'Profil Lulusan'
    }

    return render(request, template_name, context)