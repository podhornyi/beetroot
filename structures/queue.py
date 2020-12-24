from dataclasses import dataclass, field
from typing import Any


@dataclass
class Queue:
    __data: list[Any] = field(default_factory=list, init=False)

    def add(self, element):
        self.__data.append(element)

    def get(self):
        if self.__data:
            element = self.__data[0]
            self.__data = self.__data[1:]
            return element
        raise Exception('Can not get from empty queue')