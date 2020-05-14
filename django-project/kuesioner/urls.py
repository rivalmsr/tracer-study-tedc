from django.urls import path
from .views import KuesionerHome

app_name = 'kuesioner'
urlpatterns = [
    path('', KuesionerHome.as_view(), name='form-ts'),
]
