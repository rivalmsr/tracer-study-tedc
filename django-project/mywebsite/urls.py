from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('respons/', include('respons.urls', namespace='respons')),
    path('lulusan/', include('lulusan.urls', namespace='lulusan')),
    path('kuesioner/', include('kuesioner.urls', namespace='kuesioner')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
]
