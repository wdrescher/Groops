from django.urls import path, include
from appOne import views

urlpatterns = [
    path('',views.index),
    path('result/', views.result),
    path('result/<int:pk>', views.detail),
]
