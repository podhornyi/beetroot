from dataclasses import dataclass, field
from typing import Any


@dataclass
class Stack:
    __data: list[Any] = field(default_factory=list, init=False)

    def push(self, element):
        self.__data.append(element)

    def pop(self):
        if self.__data:
            return self.__data.pop()
        return None

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.__data)
