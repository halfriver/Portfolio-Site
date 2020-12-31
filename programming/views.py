from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, View
from django.http import HttpResponse
from programming.models import Program
from django.templatetags.static import static
from random import choice
from myportsite.settings import BASE_DIR
import os


class MainProgram(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = "programs"

    def get_queryset(self, **kwargs):
        queryset = Program.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def plain_text_view(code):
        f = open(code, 'r')
        content = f.read()
        f.close()
        return HttpResponse(content, content_type='text/plain')


class Dict(View):
    def get(self, request, *args, **kwargs):
        dict = static('files/dictionary.txt')
        print(BASE_DIR)
        f = open(BASE_DIR + dict, "r")
        choices = f.read().split()
        f.close()
        word = choice(choices)

        return HttpResponse(word)
