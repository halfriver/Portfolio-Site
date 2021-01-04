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
        queryset = Program.objects.all().order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_program_text():
        with open(template_name, 'r') as f:
            program_text = f.readlines()
        return HttpResponse(program_text)


class Dict(View):
    def get(self, request, *args, **kwargs):
        dict = static('files/dictionary.txt')
        f = open(BASE_DIR + dict, "r")
        choices = f.read().split()
        f.close()
        word = choice(choices)

        return HttpResponse(word)
