from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from programming.models import Program

class MainProgram(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = "programs"

    def get_queryset(self, **kwargs):
        queryset = Program.objects.all()
        return queryset

    # **kwargs = can take any number of keyword arguments, without needing to specify them
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    # context_object_name = "cv"

class Armstrong(TemplateView):
    template_name = "armstrong.html"
