from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("poem_generation", views.poem_generation),
    path("sarcastic_news", views.sarcastic_news),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)