from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from cv.models import CVDoc

class MainCV(TemplateView):
    model = CVDoc
    # context_object_name = "cv"
