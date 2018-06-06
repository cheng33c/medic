from django.urls import path

from .views import IndexView, DetailView

app_name = 'medical_record'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view, name='detail'),
]