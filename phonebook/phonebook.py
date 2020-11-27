"""
SSL issue fix:
https://stackoverflow.com/questions/44649449/brew-installation-of-python-3-6-1-ssl-certificate-verify-failed-certificate/44649450#44649450
"""

from datetime import datetime
import time
import random
import sys

from phonebook.optimized_phonebook import OptimizedPhoneBook, Person
from phonebook.simple_phonebook import SimplePhoneBook

from randomuser import RandomUser


class PhoneBook:
    PHONEBOOK_MENU = [
        '1. Generate random X users',
        '2. Search by first name',
        '3. Search by last name',
        '4. Search by full name',
        '5. Search by phone',
        '6. Search by city',
        '7. Update by phone',
        '8. Delete by phone',
        '9. Exit'
    ]

    def __init__(self, name: str, auto_create: bool = False):
        self._simple_phonebook = SimplePhoneBook(f'simple_{name}.json', auto_create=auto_create)
        self._optimized_phonebook = OptimizedPhoneBook(f'optimized_{name}.json', auto_create=auto_create)

        self._phonebook_actions = {
            1: self.generate_random_users,
            2: self.search_by_first_name,
            3: self.search_by_last_name,
            4: self.search_by_full_name,
            5: self.search_by_phone,
            6: self.search_by_city,
            7: self.update_by_phone,
            8: self.delete_by_phone,
            9: self.exit,
            -1: self._performance_test
        }
        print(f'Total contacts in simple phonebook is {len(self._simple_phonebook.phonebook)}')
        print(f'Total contacts in optimized phonebook is {len(self._optimized_phonebook._phonebook)}')

    def run(self):
        try:
            print('\n'.join(self.PHONEBOOK_MENU), '\n\n', '='*30)
            while True:
                action = self._phonebook_actions.get(
                    self._get_parsed_int('Please choose action ')
                )

                if not action:
                    print('Wrong action number')
                    continue

                action()
        finally:
            self._simple_phonebook.save()
            self._optimized_phonebook.save()

    def generate_random_users(self):
        qty = self._get_parsed_int('How many users? ')
        self._generate_random_users(qty)
        print(f'Added {qty} random users')

    def search_by_first_name(self):
        first_name = input('Enter first name: ')
        result = self._optimized_phonebook.search_by_first_name(first_name)
        if not result:
            print('Not found')
        else:
            print('\n'.join(result))

    def search_by_last_name(self):
        last_name = input('Enter last name: ')
        result = self._optimized_phonebook.search_by_last_name(last_name)
        if not result:
            print('Not found')
        else:
            print('\n'.join(result))

    def search_by_phone(self):
        phone = input('Enter phone: ')
        result = self._optimized_phonebook.search_by_phone(phone)
        if not result:
            print('Not found')
        else:
            print('\n'.join(result))

    def search_by_full_name(self):
        full_name = input('Enter full name: ')
        result = self._optimized_phonebook.search_by_full_name(full_name)
        if not result:
            print('Not found')
        else:
            print('\n'.join(result))

    def search_by_city(self):
        city = input('Enter city: ')
        result = self._optimized_phonebook.search_by_city(city)
        if not result:
            print('Not found')
        else:
            print('\n'.join(result))

    def update_by_phone(self):
        phone = input('Enter phone: ')
        result = self._optimized_phonebook.search_by_phone(phone)
        if result:
            contacts = '\n'.join(result)
            if input(f'All these contacts:\n{contacts}\nwill be updated with your values, are you sure? (Y/n)') == 'Y':
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                city = input('City: ')
                self._update_simple_phonebook(phone, first_name, last_name, city)
                self._update_optimized_phonebook(phone, first_name, last_name, city)
        else:
            print('Nothing to update')

    def delete_by_phone(self):
        phone = input('Enter phone: ')
        result = self._optimized_phonebook.search_by_phone(phone)
        if result:
            contacts = '\n'.join(result)
            if input(f'All these contacts:\n{contacts}\nwill be DELETED, are you sure? (Y/n)') == 'Y':
                self._simple_phonebook.delete(phone)
                self._optimized_phonebook.delete(phone)
        else:
            print('Nothing to delete')

    def exit(self):
        sys.exit()

    def _update_simple_phonebook(self, phone: str, first_name: str, last_name: str, city: str):
        self._simple_phonebook.update(
            phone,
            dict(
                first_name=first_name,
                last_name=last_name,
                city=city
            )
        )

    def _update_optimized_phonebook(self, phone: str, first_name: str, last_name: str, city: str):
        self._optimized_phonebook.update(
            phone,
            Person(
                first_name=first_name,
                last_name=last_name,
                city=city
            )
        )

    @staticmethod
    def _get_parsed_int(input_message: str, error_message: str = 'Not an integer, try again\n'):
        while 1:
            try:
                return int(input(input_message))
            except Exception:
                print(error_message)

    def _generate_random_users(self, qty: int = 1000):
        for user in self._get_random_users(qty):
            self._add_user_to_simple_phonebook(user)
            self._add_user_to_optimized_phonebook(user)

    @staticmethod
    def _get_random_users(qty: int = 1000):
        while True:
            try:
                return RandomUser.generate_users(qty, get_params=dict(nat='GB'))
            except Exception:
                print('Sleeping 1 sec and trying again')
                time.sleep(1)

    def _add_user_to_simple_phonebook(self, user: RandomUser):
        self._simple_phonebook.add_person(
            dict(
                first_name=user.get_first_name(),
                last_name=user.get_last_name(),
                phone=user.get_phone(),
                city=user.get_city()
            )
        )

    def _add_user_to_optimized_phonebook(self, user: RandomUser):
        self._optimized_phonebook.add_person(
            Person(
                first_name=user.get_first_name(),
                last_name=user.get_last_name(),
                city=user.get_city(),
                phone=user.get_phone()
            )
        )

    def _performance_test(self):
        print(
            '''
            Performance tests
            
            Fill phonebooks with 10k contacts
            
            For each phonebook (simple and optimized):
            1. Search random 50 users
            2. Update random 50 users
            3. Delete random 50 users
            '''
        )
        print('Fill phonebooks with 10k contacts')
        for _ in range(10):
            self._generate_random_users(1000)

        print(f'Simple phonebook contains {len(self._simple_phonebook.phonebook)} contacts')
        print(f'Optimized phonebook contains {len(self._optimized_phonebook._phonebook)} contacts')

        print('Get random 50 users')
        ids = set()
        while len(ids) != 50:
            ids.add(random.randint(0, len(self._simple_phonebook.phonebook) - 1))

        start_time = datetime.utcnow()
        for id in ids:
            contact = self._simple_phonebook.phonebook[id]
            self._simple_phonebook.search_by_first_name(contact['first_name'])
            self._simple_phonebook.update(contact['phone'], dict(last_name='Changed last name'))
            self._simple_phonebook.delete(contact['phone'])

        simple_phonebook_time = datetime.utcnow() - start_time

        start_time = datetime.utcnow()
        for id in ids:
            contact = self._optimized_phonebook._phonebook[id]
            self._optimized_phonebook.search_by_first_name(contact.first_name)
            self._optimized_phonebook.update(contact.phone, Person(first_name='Test first name'))
            self._optimized_phonebook.delete(contact.phone)

        optimized_phonebook_time = datetime.utcnow() - start_time
        print('Performance test results:')
        print(f'Simple phonebook {simple_phonebook_time}')
        print(f'Optimized phonebook {optimized_phonebook_time}, ratio {simple_phonebook_time / optimized_phonebook_time}')
