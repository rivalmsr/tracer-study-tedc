from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth import ( 
    authenticate, 
    login as auth_login,
    logout as auth_logout,
)
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from kuesioner.models import (
    MasterKuesioner,
    MasterSubKuesioner,
    MasterOpsiRespons,
    MasterFSatu,
)
from django.contrib.auth.models import User
from respons.models import (
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

def beranda(request):
    template_name = 'beranda.html'
    # list of lulusan
    list_of_lulusan = MasterFSatu.objects.all()
    total_lulusan = list_of_lulusan.count()
    # list of user confirmasi
    list_of_user = User.objects.all()
    list_of_user_isActive = User.objects.filter(is_active=True)
    persentase = 100 / (list_of_user.count() - 1)
    user_confirmation_email = round((list_of_user_isActive.count() - 1) * persentase)
    # data bar chat
    list_of_prodi = ResponsFDelapanDetail.objects.values_list('respons_header_id__master_fsatu_id__master_prodi_id__nama', flat=True).order_by('respons_header_id__master_fsatu_id__master_prodi_id__pk').distinct()
    list_lulusan_belum_bekerja = []
    list_lulusan_sudah_bekerja = []
    for prodi in list_of_prodi:
        prodi_respons_ya = ResponsFDelapanDetail.objects.filter(respons_header_id__master_fsatu_id__master_prodi_id__nama=prodi, respons='Ya').count()
        prodi_respons_tidak = ResponsFDelapanDetail.objects.filter(respons_header_id__master_fsatu_id__master_prodi_id__nama=prodi, respons='Tidak').count()
        list_lulusan_sudah_bekerja.append(prodi_respons_ya)
        list_lulusan_belum_bekerja.append(prodi_respons_tidak)
    
    # respons header
    list_of_responden =  ResponsHeader.objects.all().count()
    if list_of_responden > 0:
        persentase = 100 / list_of_lulusan.count()
        responden_completed = ResponsHeader.objects.filter(completed=True).count()
        responden_process = ResponsHeader.objects.filter(completed=False).count()
        
        persentase_respons_completed = round(responden_completed * (100 / (list_of_lulusan.count()-responden_process)))
        persentase_respons_process = round(responden_process * (100 / (list_of_lulusan.count()-responden_completed)))
    else:
        persentase_respons_completed = 0
        persentase_respons_process = 0
    context       = {
        'title': 'Beranda',
        'total_lulusan': total_lulusan,
        'user_confirmation_email': user_confirmation_email,
        'persentase_respons_completed': persentase_respons_completed,
        'persentase_respons_process': persentase_respons_process,
        'list_of_prodi': list_of_prodi,
        'list_lulusan_sudah_bekerja': list_lulusan_sudah_bekerja,
        'list_lulusan_belum_bekerja': list_lulusan_belum_bekerja,
        'nav_status_beranda': 'active',
    }

    return render(request, template_name, context)

def login_view(request):
    template_name = 'login.html'
    form = AuthenticationForm()
    context = {
        'title': 'Halaman Login',
        'form': form,
    }
    user = None
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        else :
            return render(request, template_name, context)
    
    
    if request.method == 'POST':
        username_login = request.POST.get('username')
        password_login = request.POST.get('password')
        user = authenticate(request, username= username_login, password=password_login)
        if user is not None:

            form = auth_login(request, user)
            messages.success(request, f'welcome {username_login} !!')
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else :
                return redirect('beranda')
        else:
            messages.info(request, f'Akun Tracer Study belum terdaftar!')
            return redirect('login')

def logout_view(request):
    auth_logout(request)
    return redirect('login')