from django.urls import path

from .views import IndexView, DetailView, get_medical_record_page

app_name = 'medical_record'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('add/', get_medical_record_page, name='add'),
]