from django.shortcuts import render
from . forms import (
    ReportHorizontalAndVerticalForm
)

def index(request):
    pass

def report_horizontal(request):
    template_name = 'report/report_form.html'
    report_form = ReportHorizontalAndVerticalForm(request.POST or None)
    context = {
        'title': 'Report Keselarasan Horisontal',
        'report_form': report_form,
    }
    return render(request, template_name, context)

def report_vertical(request):
    template_name = 'report/report_form.html'
    report_form = ReportHorizontalAndVerticalForm(request.POST or None)
    context = {
        'title': 'Report Keselarsan Vertikal',
        'report_form': report_form,
    }
    return render(request, template_name, context)

def report_waiting_list(request):
    pass
