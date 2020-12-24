from dataclasses import dataclass, field
from typing import Any


@dataclass
class Deque:
    __data: list[Any] = field(default_factory=list, init=False)

    def add(self, element):
        self.__data.append(element)

    def add_first(self, element):
        self.__data = [element] + self.__data

    def get(self):
        if self.__data:
            element = self.__data[0]
            self.__data = self.__data[1:]
            return element
        raise Exception('Can not get from empty deque')

    def get_last(self):
        if self.__data:
            element = self.__data[len(self.__data) - 1]
            self.__data = self.__data[:-1]
            return element
        raise Exception('Can not get_last from empty deque')