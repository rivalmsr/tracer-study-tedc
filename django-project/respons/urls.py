from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    index,
    detail,
    create,
    update,
    ResponsListView,
)


app_name = 'respons'
urlpatterns = [
    path('list/', login_required(ResponsListView.as_view()), name='list'),
    path('detail/<int:detail_id>/', login_required(detail), name='detail'),
    path('update/<int:update_id>/', login_required(update), name='update'),
    path('create/', login_required(create), name='create'),
    path('', login_required(index), name='index'),
]
