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


class BerandaView(TemplateView):
    template_name = 'base.html'
    extra_context       = {
        'title': 'Beranda',
        'nav_status_beranda': 'active',
    }

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
            messages.info(request, f'account done not exit please sing in!')
            return redirect('login')

def logout_view(request):
    auth_logout(request)
    return redirect('login')