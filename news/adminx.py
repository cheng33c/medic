import xadmin

from .models import News, Category

# Register your models here.

class CategoryAdmin(object):
    fieldssets= [
        ('分类信息', {'fields': ['name']}),
    ]


class NewsAdmin(object):
    fieldssets = [
        ('文章信息', {'fields': ['title', 'author', 'category', 'clicks_num']}),

    ]
    list_display = ('title', 'author', 'clicks_num')
    list_filter = ['title', 'author', 'category']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(News, NewsAdmin)