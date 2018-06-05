from django.utils import timezone
from django.views import generic

from .models import News

# Create your views here.

class IndexView(generic.ListView):

    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        '''返回最近的10篇文章'''
        return News.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:30]


class DetailView(generic.DetailView):

    model = News
    template_name = 'news/detail.html'

    def get_queryset(self):
        '''排除尚未发布的文章'''
        return News.objects.filter(pub_date__lte=timezone.now())