from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("abstract_art/", views.abstract_art),
    path("simpson/", views.simpson),
    path("paint/", views.paint),
    path("flowers/", views.flowers),
    path("", views.home),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)