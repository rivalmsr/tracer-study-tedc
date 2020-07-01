from django.urls import path
from .views import (
    index,
    detail,
    create,
    update,
    ResponsListView,
)


app_name = 'respons'
urlpatterns = [
    path('list/', ResponsListView.as_view(), name='list'),
    path('detail/<int:detail_id>/', detail, name='detail'),
    path('update/<int:update_id>/', update, name='update'),
    path('create/', create, name='create'),
    path('', index, name='index'),
]
