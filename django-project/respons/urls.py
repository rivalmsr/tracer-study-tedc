from django.urls import path
from django.views.generic import TemplateView
from .views import (
    index,
    create,
)


app_name = 'respons'

urlpatterns = [
    # path('create/', ResponsCreate.as_view(), name='create'),
    path('create/', create, name='create'),
    path('', index, name='index'),
]
