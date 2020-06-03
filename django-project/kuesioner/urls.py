from django.urls import path
from .views import KuesionerView

app_name = 'kuesioner'
urlpatterns = [
    path('', KuesionerView.as_view(), name='form'),
]
