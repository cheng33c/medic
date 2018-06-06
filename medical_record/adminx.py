import xadmin

from .models import MedicalRecord

# Register your models here.

class MedicalRecordAdmin(object):
    list_display = ['title', 'create_date', 'patient', 'doctor', 'hospital']
    search_fields = ['title', 'patient', 'doctor', 'hospital']
    list_filter = ['title', 'create_date', 'patient', 'doctor', 'hospital']

    class Meta:
        verbose_name = '病历管理'
        verbose_name_plural = verbose_name


xadmin.site.register(MedicalRecord, MedicalRecordAdmin)