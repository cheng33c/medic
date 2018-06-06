from ckeditor.fields import RichTextField

from django.db import models
from django.utils import timezone

from hospital.models import Hospital
from users.models import Users, Doctors

# Create your models here.


class MedicalRecordManager(models.Manager):
    pass


class MedicalRecord(models.Model):
    title = models.CharField(max_length=50, verbose_name='病历标题', default='', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='病历创建时间', default=timezone.datetime.now)
    patient = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='病人')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='医生')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='创建病历时所属医院')
    desc = RichTextField(verbose_name='病历内容')


    class Meta:
        verbose_name = '病历'
        verbose_name_plural = verbose_name
