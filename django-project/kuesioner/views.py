from django.shortcuts import render
from django.views.generic import TemplateView

class KuesionerHome(TemplateView):
    template_name = 'kuesioner/kuesioner_form_ts.html'


