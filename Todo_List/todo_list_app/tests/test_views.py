from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from todo_list_app.models import Task
from django.urls import reverse


class BasicTest(APITestCase):

    def test_get_all_todos(self):
        #booking_date = date.today() + timedelta(days=10)
        #response = self.client.get(f'/parking/parkinglot/?=${booking_date}')
        response = self.client.get('/api/v1/tasks/all/')
        self.assertEqual(response.status_code, 200)

class ApiViewsTests(APITestCase):

    url = reverse('get_by_id_task', args=[1])

    def test_get_by_id_todos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

        #given
        task = Task(title='title', is_done=True, desc='desc')
        task.save()
        #when
        response = self.client.get(self.url)
        #then
        self.assertEqual(response.status_code, 200)


    #def test_update_by_id_todos(self):


class DeleteViewTest(APITestCase):

    url = reverse('get_by_id_task', args=[1])

    def test_delete_by_id_todos(self):
        # given
        task = Task(title='title', is_done=True, desc='desc')
        task.save()


        # when
        #response = self.client.delete(self.url)

        response = self.client.delete(reverse('get_by_id_task', kwargs={'pk': task.pk}), follow=True)
        # then
        self.assertEqual(response.status_code, 204)

class PutViewTest(APITestCase):

    url = reverse('get_by_id_task', args=[1])

    def test_delete_by_id_todos(self):
        # given
        task = Task(title='title', is_done=True, desc='desc')
        task.save()

        data = {

            "title": "ed",
            "is_done": True,
            "desc": "I am working"
        }

        response = self.client.put(reverse('get_by_id_task', kwargs={'pk': task.pk}), data, format='json')
        self.assertEqual(response.status_code, 200)

        task.refresh_from_db()
        self.assertEqual('ed', task.title)



class CreateViewTest(APITestCase):

    create_url = reverse('create-task')

    def test_create_task_todos(self):
        data = {

            "title": "ed",
            "is_done": True,
            "desc": "I am working"
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, 200)














