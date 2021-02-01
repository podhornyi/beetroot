from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self._data = data
        self._root: Optional[Node] = None
        self._left: Optional[Node] = None
        self._right: Optional[Node] = None

    def set_root(self, node: 'Node') -> None:
        self._root = node

    def set_left(self, node: 'Node') -> None:
        self._left = node

    def set_right(self, node: 'Node') -> None:
        self._right = node

    def __str__(self):
        return str(self._data)

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def is_root(self):
        return self._root is None

    @property
    def is_leaf(self):
        return self._left is None and self._right is None
