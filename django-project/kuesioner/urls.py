from django.urls import path
from .views import (
    KuesionerIndex,
    KuesionerForm,
    KuesionerView,
)

app_name = 'kuesioner'
urlpatterns = [
    path('form/', KuesionerForm.as_view(), name='form'),
    path('', KuesionerIndex.as_view(), name='index'),
]
