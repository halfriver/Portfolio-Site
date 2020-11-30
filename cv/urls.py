from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainCV.as_view(), name='main_cv'),
    # path('<slug:name>/', views.CharacterDetail.as_view())
]
