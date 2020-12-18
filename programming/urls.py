from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainProgram.as_view(), name='main_program'),
    path('hangman-dict/', views.Dict.as_view())
]
