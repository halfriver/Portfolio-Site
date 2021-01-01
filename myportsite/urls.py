from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('resume/', include('cv.urls')),
    path('programming/', include('programming.urls')),
    path('art/', include('art.urls')),
    path('contact/', include('contact.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
