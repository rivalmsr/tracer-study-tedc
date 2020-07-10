from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    KuesionerIndex,
    KuesionerListView,
    KuesionerDetailView,
)

app_name = 'kuesioner'
urlpatterns = [
    path('list/', login_required(KuesionerListView.as_view()), name='list'),
    path('detail/<slug:slug>/', login_required(KuesionerDetailView.as_view()), name='detail'),
    path('', login_required(KuesionerIndex.as_view()), name='index'),
]
