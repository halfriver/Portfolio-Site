from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from programming.models import Program

class MainProgram(TemplateView):
    model = Program
    template_name = "programs.html"
    # context_object_name = "cv"
