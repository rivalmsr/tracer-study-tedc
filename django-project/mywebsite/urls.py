from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth.decorators import login_required
from .views import (
    login_view,
    logout_view,
    beranda,
    home
)
urlpatterns = [
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/login/', login_view, name='login' ),
    path('report/', include('report.urls', namespace='report')),
    path('respons/', include('respons.urls', namespace='respons')),
    path('lulusan/', include('lulusan.urls', namespace='lulusan')),
    path('kuesioner/', include('kuesioner.urls', namespace='kuesioner')),
    path('admin/', admin.site.urls),
    path('beranda/', login_required(beranda), name='beranda'),
    path('', home, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)