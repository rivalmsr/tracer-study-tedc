from django.urls import path
from .views import (
    index,
    report_horizontal,
    report_vertical,
    report_waiting_list,
)

app_name = 'report'
urlpatterns = [
    path('daftar-lama-tunggu/', report_waiting_list, name="waiting_list"),
    path('keselaransan-vertikal/', report_vertical, name='vertical'),
    path('keselarasan-horisontal/', report_horizontal, name="horizontal"),
    path('', index, name="index"),    
]
