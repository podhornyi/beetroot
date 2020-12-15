from unittest import TestCase
from unittest.mock import patch, MagicMock

from main import User


class TestBoss(TestCase):

    def test_user_name(self):
        name = 'qwerty'
        user = User(name)
        self.assertEquals(name, user.name)

    @patch('builtins.input')
    def test_get_user_age(self, mocked_input):
        mocked_input.return_value = '33'
        user = User('')
        self.assertEqual('33', user.get_age())

    @patch('main.User.get_user_data')
    def test_get_user_data(self, mocked_get_user_data):
        user = User('')
        desired_value = 2
        mocked_get_user_data.return_value = 2
        self.assertEqual(desired_value, user.get_user_data())

    @patch('main.User.get_last_name')
    @patch('main.User.get_dog_name')
    def test_get_user_data_v2(self, mocked_get_dog_name, mocked_get_last_name):
        user = User('')
        mocked_get_dog_name.return_value = 'Alex'
        mocked_get_last_name.return_value = 'Ololoevich'
        self.assertEqual(('Ololoevich', 'Alex'), user.get_user_data())


