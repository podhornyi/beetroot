from dataclasses import dataclass, field
from typing import Any


@dataclass
class Queue:
    __data: list[Any] = field(default_factory=list, init=False)

    def add(self, element):
        self.__data.append(element)

    def get(self):
        if self.__data:
            return self.__data[0]
        raise Exception('Can not get from empty queue')