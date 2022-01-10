from django.urls import path
from . import views

urlpatterns = [
    path('iris/', views.iris),
    # path('iris/ans/',views.iris_ans),

    path('heart/', views.heart),
    path('heart/ans/', views.heart_ans),
]