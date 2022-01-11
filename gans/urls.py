from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("abs_art/", views.abs_art),
    path("", views.home),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)