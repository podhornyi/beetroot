import json
import os


class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return o.asdict()

        return super().default(o)(self, o)


class Person:

    def __init__(self, first_name: str, last_name: str = None, phone: str = None, city: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.city = city

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.phone} - {self.city}'

    def __eq__(self, other):
        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.city == other.city and \
               self.phone == other.phone

    def asdict(self):
        return dict(
            first_name=self.first_name,
            last_name=self.last_name,
            city=self.city,
            phone=self.phone,
            full_name=self.get_full_name()
        )


class OptimizedPhoneBook:

    """
    {
        "data": [Person],
        "indices": {
            "ind_first_name": {
                "fist_name_1": id_1,
                "fist_name_2": id_2,
                ....
                "fist_name_n": id_n,
            },
            "ind_last_name": {},
            "ind_phone": {},
            "ind_city": {},
            "ind_full_name": {}
        }
    }

    """
    def __init__(self, name: str, auto_create: bool = False):
        self.name = name

        file_exists = os.path.exists(self.name)

        if file_exists:
            with open(self.name) as f:
                data = f.read()
                self._data = json.loads(data) if data else dict()
        elif auto_create:
            with open(self.name, 'w'):
                pass
            self._data = dict()
        else:
            raise Exception(f'File "{name}" does not exists')

        self._phonebook = [
            Person(
                first_name=person['first_name'],
                last_name=person['last_name'],
                city=person['city'],
                phone=person['phone']
            )
            for person in self._data.get('data', list())
        ]
        self._indices = self._data.get('indices', dict())

    def add_person(self, person: Person):
        self._phonebook.append(person)
        id = len(self._phonebook) - 1

        self._add_index_data('ind_first_name', person.first_name, id)
        self._add_index_data('ind_last_name', person.last_name, id)
        self._add_index_data('ind_full_name', person.get_full_name(), id)
        self._add_index_data('ind_phone', person.phone, id)
        self._add_index_data('ind_city', person.city, id)

    def search_by_first_name(self, first_name: str):
        return self._search_by_index('ind_first_name', first_name)

    def search_by_last_name(self, last_name: str):
        return self._search_by_index('ind_last_name', last_name)

    def search_by_full_name(self, full_name: str):
        return self._search_by_index('ind_full_name', full_name)

    def search_by_phone(self, phone: str):
        return self._search_by_index('ind_phone', phone)

    def search_by_city(self, city: str):
        return self._search_by_index('ind_city', city)

    def update(self, phone: str, person: Person):
        phone_index = self._indices.get('ind_phone', dict())
        ids = phone_index.get(phone, list())
        for id in ids:
            stored_person = self._phonebook[id]
            if stored_person == person:
                continue

            self._update_person(stored_person, person, id)

    def delete(self, phone: str):
        phone_index = self._indices.get('ind_phone', dict())
        ids = phone_index.get(phone, list())
        for id in ids:
            person = self._phonebook[id]
            self._remove_all_index_data(person, id)
            # need to optimized delete, because of all array elements will move...
            # del self._phonebook[id]

    def save(self):
        with open(self.name, 'w') as f:
            f.write(
                json.dumps(
                    dict(data=self._phonebook, indices=self._indices),
                    ensure_ascii=True,
                    indent=4,
                    cls=PersonEncoder
                )
            )

    def _add_index_data(self, index_name: str, key: str, id: int):
        index_data = self._indices.get(index_name, dict())
        ids = index_data.get(key, list())
        ids.append(id)

        index_data[key] = ids
        self._indices[index_name] = index_data

    def _remove_index_data(self, index_name: str, key: str, id: int):
        index_data = self._indices.get(index_name, dict())
        ids = index_data.get(key, list())
        try:
            ids.remove(id)
        except Exception:
            # Should skip. Case when delete person by phone
            pass

        index_data[key] = ids
        self._indices[index_name] = index_data

    def _update_person(self, old_person: Person, new_person: Person, person_position: int):
        first_name = last_name = city = None
        if old_person.first_name != new_person.first_name and new_person.first_name is not None:
            first_name = new_person.first_name
            self._add_index_data('ind_first_name', new_person.first_name, person_position)
            self._remove_index_data('ind_first_name', old_person.first_name, person_position)

        if old_person.last_name != new_person.last_name and new_person.last_name is not None:
            last_name = new_person.last_name
            self._add_index_data('ind_last_name', new_person.last_name, person_position)
            self._remove_index_data('ind_last_name', old_person.last_name, person_position)

        if old_person.city != new_person.city and new_person.city is not None:
            city = new_person.city
            self._add_index_data('ind_city', new_person.city, person_position)
            self._remove_index_data('ind_city', old_person.city, person_position)

        if old_person.get_full_name() != new_person.get_full_name() and new_person.first_name is not None \
                and new_person.last_name is not None:
            self._add_index_data('ind_full_name', new_person.get_full_name(), person_position)
            self._remove_index_data('ind_full_name', old_person.get_full_name(), person_position)

        self._phonebook[person_position] = Person(
            first_name=first_name or old_person.first_name,
            last_name=last_name or old_person.last_name,
            city=city or old_person.city,
            phone=old_person.phone,
        )

    def _search_by_index(self, index_name: str, key: str):
        ids = self._indices[index_name].get(key, list())
        results = []
        for id in ids:
            results.append(str(self._phonebook[id]))
        return results

    def _remove_all_index_data(self, person: Person, id: int):
        self._remove_index_data('ind_first_name', person.first_name, id)
        self._remove_index_data('ind_last_name', person.last_name, id)
        self._remove_index_data('ind_full_name', person.get_full_name(), id)
        self._remove_index_data('ind_phone', person.phone, id)
        self._remove_index_data('ind_city', person.city, id)
