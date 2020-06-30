from django.urls import path
from .views import (
    index,
    create,
    update,
    ResponsListView,
)


app_name = 'respons'
urlpatterns = [
    path('list/', ResponsListView.as_view(), name='list'),
    path('update/<int:update_id>/', update, name='update'),
    path('create/', create, name='create'),
    path('', index, name='index'),
]
