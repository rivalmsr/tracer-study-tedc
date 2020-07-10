from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import (
    login_view,
    logout_view,
    BerandaView,
)
urlpatterns = [
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/login/', login_view, name='login' ),
    path('respons/', include('respons.urls', namespace='respons')),
    path('lulusan/', include('lulusan.urls', namespace='lulusan')),
    path('kuesioner/', include('kuesioner.urls', namespace='kuesioner')),
    path('admin/', admin.site.urls),
    path('beranda/', login_required(BerandaView.as_view()), name='beranda'),
    path('', TemplateView.as_view(template_name='home.html'), name='index'),
]
