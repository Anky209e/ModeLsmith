from django.urls import path
from . import views

urlpatterns = [
    path('iris/', views.iris),
    path('heart/', views.heart),
]