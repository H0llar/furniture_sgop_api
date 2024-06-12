from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.serializers import UserSerializer

UserModel = get_user_model()


class CreateUserViewTest(APITestCase):
    url = '/api/auth/registration/'

    valid_data = {
        'username': 'test',
        'password': 'a$kjsASd78',
        'first_name': 'Johan',
        'last_name': 'Smith',
    }

    def setUp(self):
        self.existed_user = UserModel.objects.create_user(username='user',
                                                          password='<PASSWORD>',
                                                          first_name='John', last_name='Doe')

    def test_valid_create(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        serializer = UserSerializer(UserModel.objects.get(id=response.data['id']))
        self.assertDictEqual(response.data, serializer.data)

    def test_invalid_existed_user(self):
        response = self.client.post(self.url, data={**self.valid_data, 'username': 'user'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_password(self):
        response = self.client.post(self.url, data={**self.valid_data, 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
