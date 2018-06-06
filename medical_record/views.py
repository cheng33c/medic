from django.shortcuts import render
from django.views import generic

from .models import MedicalRecord

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'medical_record/index.html'
    context_object_name = 'medical_record_list'

    def get_queryset(self):
        ''' 返回某个用户的所有病历 '''
        return MedicalRecord.objects.filter(user__id=self.request.userid).order_by('-create_date')


class DetailView(generic.DetailView):

    model = MedicalRecord
    template_name = 'medical_record/detail.html'


def get_medical_record_page(request):
    return render(request, 'medical_record/add_medical_record.html')


