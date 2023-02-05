from rest_framework.test import APITestCase

from todo_list_app.models import Task


class BasicTest(APITestCase):
    def test_get_all_todos(self):
        #booking_date = date.today() + timedelta(days=10)
        #response = self.client.get(f'/parking/parkinglot/?=${booking_date}')
        response = self.client.get('/api/v1/tasks/all/')
        self.assertEqual(response.status_code, 200)

    def test_get_by_id_todos(self):
        response = self.client.get('/api/v1/tasks/1')
        self.assertEqual(response.status_code, 404)

        #given
        task = Task(title='title', is_done=True, desc='desc')
        task.save()
        #when
        response = self.client.get('/api/v1/tasks/1')
        #then
        self.assertEqual(response.status_code, 200)

    def test_create_task_todos(self):
        data = {

            "title": "ed",
            "is_done": True,
            "desc": "I am working"
        }
        response = self.client.post('/api/v1/tasks/create/', data)
        print(response.json())
        self.assertEqual(response.status_code, 200)
