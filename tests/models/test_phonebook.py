import unittest

from phonebook.simple_phonebook import SimplePhoneBook


class TestSimplePhoneBook(unittest.TestCase):
    phonebook_name = 'TestSimplePhoneBook.json'

    @classmethod
    def setUpClass(cls) -> None:
        cls.simple_phonebook = SimplePhoneBook(cls.phonebook_name, auto_create=True)
        cls.test_person = {
            "first_name": "name2",
            "last_name": "name2",
            "phone": "name2",
            "city": "name2",
        }

    @classmethod
    def tearDownClass(cls) -> None:
        # delete phonebook_name
        pass

    def setUp(self) -> None:
        self.simple_phonebook.add_person(self.test_person)
        print('PERSONS', self.simple_phonebook.phonebook)

    def tearDown(self) -> None:
        self.simple_phonebook.delete(self.test_person['phone'])

    def test_get_by_name(self):

        self.assertEqual(
            [(0, self.test_person)],
            self.simple_phonebook.search_by_first_name(
                self.test_person['first_name']
            )
        )

    def test_get_by_name1(self):
        self.assertEqual(
            [(0, self.test_person)],
            self.simple_phonebook.search_by_first_name(
                self.test_person['first_name']
            )
        )


