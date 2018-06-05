import xadmin
from xadmin import views

from .models import Doctors, Users

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'Medic管理系统'
    site_footer = 'Medic'
    menu_style = 'accordion'


class UsersAdmin(object):
    fieldsets = [
        ('用户信息', {'fields': ['username', 'password', 'email'], 'classes': ['collapse']}),
        ('其他信息', {'fields': ['gender', 'mobile', 'image', 'is_active'], 'classes': ['collapse']})
    ]
    list_display = ['username', 'gender', 'email']
    search_fields = ['username', 'gender', 'email']
    list_filter = ['username', 'gender', 'email']

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


class DoctorsAdmin(object):
    list_display = ['user', 'hospital', 'work_years', 'title', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['user', 'hospital', 'work_years', 'title', 'points', 'click_nums', 'fav_nums']
    list_filter = ['user', 'hospital', 'work_years', 'title', 'points', 'click_nums', 'fav_nums', 'add_time']

    class Meta:
        verbose_name = '医生管理'
        verbose_name_plural = verbose_name


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Doctors, DoctorsAdmin)
xadmin.site.unregister(Users)
xadmin.site.register(Users, UsersAdmin)