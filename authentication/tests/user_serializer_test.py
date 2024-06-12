from django.contrib.auth import get_user_model
from django.test import TestCase

from authentication.serializers import UserSerializer

UserModel = get_user_model()


class UserSerializerTest(TestCase):
    valid_data = {
        'username': 'user',
        'password': 'a$sdf848#_@213kSDska',
        'first_name': 'user',
        'last_name': 'puper',
    }

    invalid_data = {
        'username': 1,
        'password': 'password',
    }

    def test_valid_serializer(self):
        serializer = UserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        serializer = UserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_create_serializer(self):
        serializer = UserSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, self.valid_data['username'])
        self.assertEqual(user.first_name, self.valid_data['first_name'])
        self.assertEqual(user.last_name, self.valid_data['last_name'])

        user_from_db = UserModel.objects.get(id=user.id)
        self.assertIsNotNone(user_from_db)

    def test_read_serializer(self):
        user = UserModel.objects.create(**self.valid_data)
        serializer = UserSerializer(user)
        expected_data = {
            'id': user.id,
            'username': self.valid_data['username'],
            'first_name': self.valid_data['first_name'],
            'last_name': self.valid_data['last_name'],
        }

        self.assertDictEqual(serializer.data, expected_data)
