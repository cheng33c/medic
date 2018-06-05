from datetime import datetime, timedelta
from ckeditor.fields import RichTextField

from django.db import models
from django.utils import timezone

from users.models import Users

# Create your models here.

class NewsManager(models.Manager):

    def query_by_category(self, category_id):
        query = self.get_queryset().filter(category_id=category_id)
        return query

    def query_by_collects(self):
        query = self.get_queryset().order_by('-collects_num')
        return query

    def query_by_time(self):
        query = self.get_queryset().order_by('-pub_date')
        return query

    def query_by_clicks(self):
        query = self.get_queryset().order_by('-clicks_num')
        return query

    def query_by_keyword(self, keyword):
        query = self.get_queryset().filter(title__contains=keyword)
        return query


class Category(models.Model):

    name = models.CharField(verbose_name='分类名', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '新闻分类'
        verbose_name_plural = verbose_name


class News(models.Model):
    ''' 新闻模型 '''
    objects = NewsManager()
    title = models.CharField(verbose_name='题目', max_length=256)
    author = models.ForeignKey(Users, null=True, on_delete=models.CASCADE, verbose_name='作者')
    content = RichTextField('内容')
    thumbup_num = models.PositiveIntegerField(default=0, verbose_name="点赞数")
    collects_num = models.PositiveIntegerField(default=0, verbose_name="收藏数")
    comments_num = models.PositiveIntegerField(default=0, verbose_name="评论数")
    clicks_num = models.PositiveIntegerField(default=0, verbose_name="点击数")
    pub_date = models.DateTimeField(verbose_name="上传日期")
    modify_date = models.DateTimeField(verbose_name="修改日期")
    is_published = models.BooleanField(verbose_name="是否上传?", default=False)
    category = models.ManyToManyField(Category, verbose_name='分类')

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = '-pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近上传？'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
