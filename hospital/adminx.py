import xadmin

from .models import City, District, Hospital, Province

# Register your models here.


class ProvinceAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

    class Meta:
        verbose_name = '省份管理'
        verbose_name_plural = verbose_name


class CityAdmin(object):
    list_display = ['name', 'province']
    search_fields = ['name', 'province']
    list_filter = ['name', 'province']

    class Meta:
        verbose_name ='城市管理'
        verbose_name_plural = verbose_name



class DistrictAdmin(object):
    list_display = ['name', 'city']
    search_fields = ['name', 'city']
    list_filter = ['name', 'city']

    class Meta:
        verbose_name = '辖区管理'
        verbose_name_plural = verbose_name


class HospitalAdmin(object):
    list_display = ['name', 'district', 'click_nums', 'fav_nums', 'points']
    search_fields = ['name', 'district', 'click_nums', 'fav_nums', 'points']
    list_filter = ['name', 'district', 'click_nums', 'fav_nums', 'points']

    class Meta:
        verbose_name = '医院管理'
        verbose_name_plural = verbose_name



xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(City, CityAdmin)
xadmin.site.register(District, DistrictAdmin)
xadmin.site.register(Hospital, HospitalAdmin)