from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainArt.as_view(), name='main_art'),
    # path('<slug:name>/', views.CharacterDetail.as_view())
]
