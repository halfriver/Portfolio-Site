from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from art.models import ArtPiece, ArtTag


class MainArt(ListView):
    model = ArtTag
    template_name = "gallery.html"
    context_object_name = "tag"

    def get_queryset(self, **kwargs):
        queryset = ArtTag.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = ArtTag.objects.values_list("name", flat=True)
        art_dict = {}
        for tag in tags:
            art_dict[tag] = ArtPiece.objects.filter(tags__name__in=[tag])
        context["art"] = art_dict
        context["all"] = ArtPiece.objects.all().order_by('-date')
        return context
