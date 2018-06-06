from django import template

from users.models import Doctors

register = template.Library()


@register.filter
def is_doctor(userid):
    return Doctors.objects.filter(user__id=userid)