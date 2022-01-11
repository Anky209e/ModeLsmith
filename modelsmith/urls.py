from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nn/', include("nn.urls")),
    path('cnn/', include("cnn.urls")),   
    path('gans/', include("gans.urls")), 
    path('', views.base), 
    path('home/', views.home), 
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
