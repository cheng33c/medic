from django.shortcuts import render, redirect
from django.views import generic

from .models import MedicalRecord
from .forms import MedicalRecordCreationForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'medical_record/index.html'
    context_object_name = 'medical_record_list'

    def get_queryset(self):
        ''' 返回某个用户的所有病历 '''
        return MedicalRecord.objects.order_by('-create_date')


class DetailView(generic.DetailView):

    model = MedicalRecord
    template_name = 'medical_record/detail.html'


def get_add_medical_record_page(request):
    return render(request, 'medical_record/add_medical_record.html')


def add_medical_record(request):
    '''添加用户病历'''
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = MedicalRecordCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = MedicalRecordCreationForm()
    return render(request, 'medical_record/add_medical_record.html', context={'form': form})

