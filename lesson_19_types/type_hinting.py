import typing
from abc import abstractmethod

def print_user_info(
        name: str, age: int, hobby: typing.List[str] = None
    ) -> None:
    print(f'My name is {name}, I am {age} age old\n'
          f'My hobbies: {hobby}')


def list_returner() -> dict[str, list[list[int]]]:
    return dict(s=[[1,2,3,4], [5,6,78]])

# print_user_info('Kola', 13, ['1', '2', '3'])


class Person:
    @abstractmethod
    def walk(self): raise NotImplementedError
    @abstractmethod
    def talk(self): raise NotImplementedError
    @abstractmethod
    def handshake(self): raise NotImplementedError


class User(Person):
    def talk(self): print('I am talking')
    def handshake(self): print('I am handshaking')
    def walk(self): print('I am walking')


user = User()


def live(person: Person):
    person.talk()
    person.handshake()
    person.walk()
    print('I am done')


print(hasattr(user, 'tal'))
live(user)

