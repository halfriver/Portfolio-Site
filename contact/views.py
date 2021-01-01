from django.views.generic import TemplateView


class MainContact(TemplateView):
    template_name = 'contact.html'
