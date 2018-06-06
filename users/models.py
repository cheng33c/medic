from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from hospital.models import Hospital

# Create your models here.


class Users(AbstractUser):
    email = models.EmailField(verbose_name='电子邮箱', null=False, blank=False,
                              unique=True, error_messages={'unique': '该电子邮箱已被占用'})
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='', verbose_name='性别')
    mobile = models.CharField(max_length=100, default='', null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to='upload/images/users/%Y/%m', null=True, blank=True,
                              default='upload/image/users/default.jpg', verbose_name='用户头像')

    def __str__(self):
        return self.username

    def is_doctor(self):
        return Doctors.objects.filter(user__id=id)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class DoctorsManager(models.Manager):

    def query_by_hospital_name(self, hospital_name):
        pass

    def query_by_userid(self, userid):
        return Doctors.objects.filter(user__id=userid)


class Doctors(models.Model):
    ''' 医生模型 继承Users模型 加上必要认证 '''
    '''
    Todo-list: 加上预约功能, 医生候诊时间
    '''
    objects = DoctorsManager()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='用户')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名', default='')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='所属医院')
    id_num = models.CharField(max_length=18, verbose_name='身份证号', default='')
    desc = models.TextField(verbose_name='医生描述')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    title = models.SmallIntegerField(default=0, verbose_name='医生职称', choices=(
        (0, '主治医师'), (1, '副主任医师'), (2, '主任医师')))
    points = models.CharField(max_length=300, verbose_name='擅长领域')
    click_nums = models.PositiveIntegerField(verbose_name='点击数', default=0)
    fav_nums = models.PositiveIntegerField(verbose_name='收藏数', default=0)
    thumbsup_nums = models.PositiveIntegerField(verbose_name='点赞数', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '医生信息'
        verbose_name_plural = verbose_name
