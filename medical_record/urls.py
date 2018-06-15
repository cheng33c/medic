from django.urls import path

from .views import IndexView, DetailView, get_add_medical_record_page
from .views import add_medical_record

app_name = 'medical_record'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('add/', get_add_medical_record_page, name='add'),
    path('add1/', add_medical_record, name='add1')
]