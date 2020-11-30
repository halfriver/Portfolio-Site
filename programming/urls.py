from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainProgram.as_view(), name='main_program'),
    # path('<slug:name>/', views.CharacterDetail.as_view())
]
