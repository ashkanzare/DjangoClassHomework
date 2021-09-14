from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from Education.models import Student, College, StudyField


class ViewTestCase(TestCase):

    def setUp(self):
        User = get_user_model()
        # create a user for login test
        User.objects.create_user(username="ali", user_type="student", password='12345')
        user = Client()

    def test_login(self):

        response = self.client.post(reverse('Education:login'),
                             {'username': 'ali', 'password': '12345', 'user_type': 'student'},
                             follow=True)
        # check response status
        self.assertEqual(response.status_code, 200)

        # check if user's login
        self.assertTrue(response.context['user'].is_active)

    def test_register(self):
        Group.objects.create(name='Student')
        college = College.objects.create(name='physics', address='karaj')
        StudyField.objects.create(name='physics', college=college)

        data = {
            'username': 'hassan',
            'password': '12345',
            'image': '',
            'phone': '9115617075',
            'first_name': 'alireza',
            'last_name': 'zare',
            'birthday': '1998-05-05',
            'address': 'karaj',
            'personal_id': '11111',
            'email': 'a@gmail.com',
            'entry_date': '2010-05-05',
            'initial-entry_date': '2010-05-05',
            'college': 1,
            'study_field': 1
        }

        response = self.client.post(reverse('Education:register'), data)

        # check response status
        self.assertEqual(response.status_code, 200)

        # check if student created or not
        stds = Student.objects.all()
        self.assertEqual(stds.count(), 1)
