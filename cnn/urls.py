from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("maleria/", views.maleria),
    path("cifar10/", views.cifar10),
    path("gender/", views.gender),
    path("eyensign/", views.eyensign),
    path("lens_structure/", views.lens_structure),
    path("ring_classifier/", views.ring_classifier),
    path("", views.home),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)