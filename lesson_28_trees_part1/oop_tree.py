from typing import Optional


class BinaryTree:

    def __init__(self, root_obj) -> None:
        self.key = root_obj
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None
        self.reverse = False

    def insert_left(self, new_node) -> None:
        self.left_child = new_node

    def insert_right(self, new_node) -> None:
        self.right_child = new_node

    def set_root_val(self, obj) -> None:
        self.key = obj

    def get_root_val(self) -> 'BinaryTree':
        return self.key

    def __repr__(self) -> str:
        reverse = '~' if self.reverse else ''
        return f"BinaryTree{reverse}({self.key}, {self.left_child}, {self.right_child})"

    def __str__(self) -> str:
        reverse = '~' if self.reverse else ''
        return f"BinaryTree{reverse}({self.key}, {self.left_child}, {self.right_child})"

    def pre_order(self) -> None:
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self) -> None:
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

    def in_order(self) -> None:
        if self.left_child:
            self.left_child.in_order()
        print(self.get_root_val())
        if self.right_child:
            self.right_child.in_order()


if __name__ == "__main__":
    tr = BinaryTree('a')
    print(tr.get_root_val())
    print(tr.get_left_child())
    tr.insert_left('b')
    print(tr.get_left_child())
    print(tr.get_left_child().get_root_val())
    tr.insert_right('c')
    print(tr.get_right_child())
    print(tr.get_right_child().get_root_val())
    tr.get_right_child().set_root_val('hello')
    print(tr.get_right_child().get_root_val())
