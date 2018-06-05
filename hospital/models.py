from datetime import datetime

from django.db import models

# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=20, verbose_name='省份')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '省份信息'
        verbose_name_plural = verbose_name


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')
    province = models.ForeignKey(Province, verbose_name='所属省份', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name

class District(models.Model):
    ''' 区域模型 '''
    name = models.CharField(max_length=20, verbose_name='行政区域')
    city = models.ForeignKey(City, verbose_name='所属城市', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '行政区域信息'
        verbose_name_plural = verbose_name


class HospitalManager(models.Manager):
    def get_queryset_order_by_level(self):
        ''' 按医院等级进行排序 '''
        return Hospital.object.order_by('-level')[:30]

    def get_queryset_by_id(self, id):
        return Hospital.object.filter(id=id)

    def get_queryset_by_name(self, hospital_name):
        return Hospital.object.filter(name=hospital_name)


class Hospital(models.Model):
    hospital_level = ((0, '三级甲(特)医院'), (1, '三级医院'), (2, '二级医院'), (3, '一级医院'))

    object = HospitalManager()
    name = models.CharField(max_length=20, verbose_name='医院名称')
    desc = models.CharField(max_length=200, verbose_name='医院描述')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='所属行政区域')
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    points = models.CharField(max_length=300, verbose_name='擅长领域', null=True, blank=True)
    image = models.ImageField(upload_to='upload/images/hospital/%Y/%m', verbose_name='医院图片', null=True, blank=True)
    level = models.SmallIntegerField(default=0, verbose_name='医院等级', choices=hospital_level)

    def __str__(self):
        return self.name

    def city_info(self):
        ret = []
        ret.append(self.district.city.id)
        ret.append(self.district.city.name)
        return ret

    def district_info(self):
        ret = []
        ret.append(self.district.id)
        ret.append(self.district.name)
        return ret

    def province_info(self):
        ret = []
        ret.append(self.district.city.province.id)
        ret.append(self.district.city.province.name)
        return ret


    class Meta:
        verbose_name = '医院信息'
        verbose_name_plural = verbose_name

