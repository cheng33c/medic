from django.views import generic

from .models import MedicalRecord

# Create your views here.

class IndexView(generic.ListView):
    template_name = ''
    context_object_name = 'medical_record_list'

    pass


class DetailView(generic.DetailView):
    model = MedicalRecord

    pass