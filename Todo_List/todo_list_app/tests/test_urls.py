from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve


class ApiUrlsTests(APISimpleTestCase):

    def test_get_create_is_resolve(self):
        url = reverse('create-task')
        print(resolve(url))

    def test_get_by_id_is_resolve(self):
        url = reverse('get_by_id_task', args=[1])
        print(resolve(url))



