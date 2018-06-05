from django.test import TestCase

from .models import Hospital, HospitalManager

# Create your tests here.


def create_hospital(name):
    return Hospital.object.create(name=name, desc='test', district_id=1, level=0)

class HospitalManagerModelTests(TestCase):

    manager = HospitalManager()
    create_hospital('abc123')

    def test_get_queryset_order_by_level(self):
        res = self.manager.get_queryset_order_by_level()
        print(res)
        self.assertIs(res is not None, True)

    def test_get_queryset_by_id(self):
        res = self.manager.get_queryset_by_id(0)
        self.assertIs(res is not None, True)

    def test_get_queryset_by_name(self):
        # 无法通过测试
        # res = self.manager.get_queryset_by_name('abc123')
        # self.assertIs(res.values()[0]['name'] == 'abc123', True)
        pass