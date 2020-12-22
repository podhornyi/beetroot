from dataclasses import dataclass, field
from typing import Any


@dataclass
class Stack:
    __data: list[Any] = field(default_factory=list, init=False)

    def push(self, element):
        self.__data.append(element)

    def pop(self):
        return self.__data[len(self.__data) - 1]