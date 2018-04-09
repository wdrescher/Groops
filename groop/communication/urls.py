from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='user-land'),
    path('userhome/<int:pk>', views.home, name='user-home'),
    path('signup/', views.signup, name="signup"),
    path('create/', views.create, name='create')
]
