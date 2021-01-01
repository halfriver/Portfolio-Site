from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainContact.as_view(), name='main_contact'),
]
