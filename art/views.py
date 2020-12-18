from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from art.models import ArtPiece, ArtTag


class MainArt(ListView):
    model = ArtTag
    template_name = "gallery.html"
    context_object_name = "tag"

    def get_queryset(self, **kwargs):
        queryset = ArtTag.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = ArtTag.objects.values_list("name", flat=True)
        print(tags)
        art_dict = {}
        for tag in tags:
            print(tag)
            art_dict[tag] = ArtPiece.objects.filter(tags__name__in=[tag])
        context["art"] = art_dict
        print(art_dict)
        return context
