from django.views import generic
from django.utils import timezone

from .models import Hospital

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'hospital/index.html'
    context_object_name = 'hospital_list'

    def get_queryset(self):
        ''' 按医院等级进行排序 '''
        return Hospital.objects.order_by('-level')[:30]


class DetailView(generic.DetailView):
    model = Hospital
    template_name = 'hospital/detail.html'
