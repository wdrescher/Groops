from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.result),
    path('result/<int:pk>', views.detail),
]
