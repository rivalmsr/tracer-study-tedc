from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('kuesioner/', include('kuesioner.urls', namespace='kuesioner')),
    path('admin/', admin.site.urls),
]
