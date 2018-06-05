from django.urls import path

from . import views
from .views import DoctorsIndexView, DoctorsDetailView

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', DoctorsIndexView.as_view(), name='doctors_index'),
    path('doctors/detail/<int:pk>/', DoctorsDetailView.as_view(), name='doctors_detail'),
    path('register/', views.register, name='register')
]
