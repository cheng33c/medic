
from django import forms
from django.utils import timezone


# title = models.CharField(max_length=50, verbose_name='病历标题', default='', null=True, blank=True)
#     create_date = models.DateTimeField(verbose_name='病历创建时间', default=timezone.datetime.now)
#     patient = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='病人')
#     doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='医生')
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='创建病历时所属医院')
#     desc = RichTextField(verbose_name='病历内容')

class MedicalRecordCreationForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    doctor = forms.CharField(label='doctor_id', max_length=10)
    patient = forms.CharField(label='patient_id', max_length=10)
    hospital = forms.CharField(label='hospital_id', max_length=10)
    create_date = forms.DateTimeField(label='create_date')
    desc = forms.Textarea()
