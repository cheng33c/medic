from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone

from .forms import RegisterForm
from .models import Doctors


# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    '''用户注册实现 登录和注销使用Django实现'''
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form})


class DoctorsIndexView(generic.ListView):

    template_name = 'doctors/index.html'
    context_object_name = 'doctors_list'

    def get_queryset(self):
        ''' 返回医生列表 '''
        return Doctors.objects.filter(
            add_time__lte=timezone.now()
        ).order_by('-add_time')[:30]


class DoctorsDetailView(generic.DetailView):

    model = Doctors
    template_name = 'doctors/detail.html'

    def get_queryset(self):
        return Doctors.objects.filter(add_time__lte=timezone.now())