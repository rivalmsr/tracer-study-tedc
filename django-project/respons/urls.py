from django.urls import path
from django.views.generic import TemplateView
app_name = 'respons'

urlpatterns = [
    path('', TemplateView.as_view(template_name='respons/respons_form.html'), name='create')
]
