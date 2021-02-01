from trees.models import Node


class BinaryTree:

    def __init__(self, root: Node = None):
        self._direct_order = []
        self._indirect_order = []
        self._symmetric_order = []
        self._root: Node = root

    def __len__(self):
        return len(self._indirect_order)

    def direct_order(self, node: Node = None):
        if not self._root:
            return
        if not node:
            node = self._root

        self._direct_order.append(node.data)
        print(node.data)

        if node.left:
            self.direct_order(node.left)
        if node.right:
            self.direct_order(node.right)

    def indirect_order(self, node: Node = None):
        if not self._root:
            return
        if not node:
            node = self._root

        if node.left:
            self.indirect_order(node.left)
        if node.right:
            self.indirect_order(node.right)

        self._indirect_order.append(node.data)
        print(node.data)

    def symmetric_order(self, node: Node = None):
        if not self._root:
            return
        if not node:
            node = self._root

        if node.left:
            self.symmetric_order(node.left)

        self._symmetric_order.append(node.data)
        print(node.data)

        if node.right:
            self.symmetric_order(node.right)

    def insert(self, node, root: Node = None):
        if not self._root:
            self._root = node
            return

        if not root:
            root = self._root

        print(f'Inserting {node}, root is {root}. Root: {root.left} <> {root.right}')
        if node.data >= root.data:
            if root.right is None:
                node.set_root(root)
                root.set_right(node)
            else:
                self.insert(node, root.right)
        else:
            if root.left is None:
                node.set_root(root)
                root.set_left(node)
            else:
                self.insert(node, root.left)