import json
import os


class SimplePhoneBook:

    """
    Structure:
    [
        {
            "first_name": "name1",
            "last_name": "name1",
            "phone": "name1",
            "city": "name1",
        },
        {
            "first_name": "name2",
            "last_name": "name2",
            "phone": "name2",
            "city": "name2",
        },
        ....
    ]

    """
    def __init__(self, name: str, auto_create: bool = False):
        self.name = name

        file_exists = os.path.exists(self.name)

        if file_exists:
            with open(self.name) as f:
                data = f.read()
                self.phonebook = json.loads(data) if data else list()
        elif auto_create:
            with open(self.name, 'w'):
                pass
            self.phonebook = list()
        else:
            raise Exception(f'File "{name}" does not exists')

    def add_person(self, person: dict):
        self.phonebook.append(person)

    def search_by_first_name(self, first_name: str):
        return self._search_by('first_name', first_name)

    def search_by_last_name(self, last_name: str):
        return self._search_by('last_name', last_name)

    def search_by_full_name(self, full_name: str):
        return self._search_by('ind_full_name', full_name)

    def search_by_phone(self, phone: str):
        return self._search_by('phone', phone)

    def search_by_city(self, city):
        return self._search_by('city', city)

    def update(self, phone: str, person: dict):
        for _, stored_person in self.search_by_phone(phone):
            stored_person.update(**person)

    def delete(self, phone: str):
        for i, _ in self.search_by_phone(phone):
            del self.phonebook[i]

    def save(self):
        with open(self.name, 'w') as f:
            f.write(
                json.dumps(
                    self.phonebook,
                    indent=2
                )
            )

    def _search_by(self, field_name: str, search_phrase: str):
        return [(i, person) for i, person in enumerate(self.phonebook) if person[field_name] == search_phrase]
