from django.urls import path
from .views import (
    index,
    create,
    ResponsListView,
)


app_name = 'respons'
urlpatterns = [
    path('list/', ResponsListView.as_view(), name='list'),
    path('create/', create, name='create'),
    path('', index, name='index'),
]
