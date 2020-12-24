from dataclasses import dataclass, field
from typing import Any


@dataclass
class Friend:
    payload: Any
    _next: 'Friend' = field(default=None, init=False)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node: 'Friend'):
        self._next = node
