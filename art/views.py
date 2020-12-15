from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from art.models import ArtPiece

class MainArt(ListView):
    model = ArtPiece
    template_name = "gallery.html"
    context_object_name = "art"

    def get_queryset(self, **kwargs):
        queryset = ArtPiece.objects.all()
        return queryset

    # **kwargs = can take any number of keyword arguments, without needing to specify them
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
