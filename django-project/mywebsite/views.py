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

def home(request):
    template_name = 'home.html'
    context = {
        'title': 'Home | Tracer Study',
    }
    return render(request, template_name, context)

def beranda(request):
    # list of lulusan
    template_name = 'beranda.html'
    list_of_lulusan = MasterFSatu.objects.all()
    total_lulusan = list_of_lulusan.count()

    # list of user confirmasi
    list_of_user = User.objects.all()
    list_of_user_isActive = User.objects.filter(is_active=True)
    persentase = 100 / (list_of_user.count() - 1)
    user_confirmation_email = round((list_of_user_isActive.count() - 1) * persentase)

    # data bar chart fdua kuesioner
    list_of_prodi = ResponsFDelapanDetail.objects.values_list('respons_header_id__master_fsatu_id__master_prodi_id__nama', flat=True).order_by('respons_header_id__master_fsatu_id__master_prodi_id__pk').distinct()
    list_of_fdua_by_prodi = ResponsFDuaDetail.objects.values_list('respons_header_id__master_fsatu_id__master_prodi_id__nama', flat=True).order_by('respons_header_id__master_fsatu_id__master_prodi_id__pk').distinct()
    list_of_sub_pertanyaan_kode = MasterSubKuesioner.objects.filter(master_kuesioner_id__kode='F2').values_list('kode', flat=True).order_by('pk')
    list_of_respons_values = {
        'Sangat Besar': 4,
        'Besar': 3,
        'Cukup Besar': 2,
        'Kurang': 1,
        'Tidak Sama Sekali': 0,
    }
    # list of perkuliahan
    list_of_perkuliahan_values = []
    list_of_demostrasi_values = []
    list_of_proyek_riset_values = []
    list_of_magang_values = []
    list_of_praktikum_values = []
    list_of_kerja_lapangan_values = []
    list_of_diskusi_values = []
    
    for prodi in list_of_fdua_by_prodi:
        print(prodi)
        for kode in list_of_sub_pertanyaan_kode:
            print(kode)
            list_of_sub_pertanyaan = ResponsFDuaDetail.objects.filter(master_subkuesioner_id__kode=kode, respons_header_id__master_fsatu_id__master_prodi_id__nama=prodi)
            respons_value = 0
            for sub_pertanyaan in list_of_sub_pertanyaan:
                print(sub_pertanyaan)
                if list_of_sub_pertanyaan.count() > 1:
                    temp_respons_value = list_of_respons_values.get(sub_pertanyaan.respons)
                    if temp_respons_value != None:
                        respons_value += temp_respons_value
                else:
                    respons_value = list_of_respons_values.get(sub_pertanyaan.respons)
            respons_value /= list_of_sub_pertanyaan.count()
            if kode == 'F2-1':
                list_of_perkuliahan_values.append(respons_value)
            elif kode == 'F2-2':
                list_of_demostrasi_values.append(respons_value)
            elif kode == 'F2-3':
                list_of_proyek_riset_values.append(respons_value)
            elif kode == 'F2-4':
                list_of_magang_values.append(respons_value)
            elif kode == 'F2-5':
                list_of_praktikum_values.append(respons_value)
            elif kode == 'F2-6':
                list_of_kerja_lapangan_values.append(respons_value)
            elif kode == 'F2-7':
                list_of_diskusi_values.append(respons_value)

    # data bar chart
    list_aja = ResponsFDelapanDetail.objects.values_list('respons_header_id__master_fsatu_id__master_prodi_id__nama', flat=True).order_by('respons_header_id__master_fsatu_id__master_prodi_id__pk').distinct()

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
        responden_progress = ResponsHeader.objects.filter(completed=False).count()
        persentase_respons_completed = round(responden_completed * persentase)
        persentase_respons_progress = round(responden_progress * persentase)
    else:
        persentase_respons_completed = 0
        persentase_respons_progress = 0
    
    context       = {
        'title': 'Beranda',
        'nav_status_beranda': 'active',
        'total_lulusan': total_lulusan,
        'user_confirmation_email': user_confirmation_email,
        'persentase_respons_completed': persentase_respons_completed,
        'persentase_respons_progress': persentase_respons_progress,
        'list_of_prodi': list_of_prodi,
        'list_lulusan_sudah_bekerja': list_lulusan_sudah_bekerja,
        'list_lulusan_belum_bekerja': list_lulusan_belum_bekerja,
        'list_of_perkuliahan_values':list_of_perkuliahan_values,
        'list_of_demostrasi_values':list_of_demostrasi_values,
        'list_of_proyek_riset_values':list_of_proyek_riset_values,
        'list_of_magang_values':list_of_magang_values,
        'list_of_praktikum_values':list_of_praktikum_values,
        'list_of_kerja_lapangan_values':list_of_kerja_lapangan_values,
        'list_of_diskusi_values':list_of_diskusi_values,
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