import operator
import re
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)

    def __len__(self):
        return len(self._container)

    def __getitem__(self, item):
        return self._container[item]


def split_math_exp_wo_spaces(expr: str) -> List[str]:
    result = []

    index = 0
    for number_string in filter(lambda x: x, re.split(r'[()+\-*/]', expr)):
        number_index = expr.index(number_string, index)
        while index < number_index:
            result.append(expr[index])
            index += 1

        index = number_index + len(number_string)
        result.append(number_string)

    while index < len(expr):
        result.append(expr[index])
        index += 1

    return result


def insert_priority(operation: str, tree: BinaryTree, parent_tree: BinaryTree = None):
    if tree.key:
        if tree.right_child:
            new_tree = BinaryTree(operation)
            tree.insert_right(new_tree)
            return new_tree
        else:
            pass
    else:
        tree.set_root_val(operation)
    return tree


def insert(operation: str, tree: BinaryTree):
    if tree.key:
        new_tree = BinaryTree(operation)
        new_tree.insert_left(tree)
        return new_tree
    else:
        tree.set_root_val(operation)
    return tree


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens = math_exp.split() if ' ' in math_exp else split_math_exp_wo_spaces(math_exp)
    print('splitted', tokens)
    current_tree: BinaryTree = BinaryTree('')
    nodes = [current_tree]

    for i in tokens:
        print('Start', i, current_tree, nodes)
        if i == '(':
            tree = BinaryTree('')
            current_tree.insert_left(tree)
            nodes.append(current_tree)
            current_tree = tree
        elif i == ')':
            current_tree = nodes.pop()
        elif i in {'+', '-', '*', '/'}:
            current_tree.set_root_val(i)
            tree = BinaryTree('')
            current_tree.insert_right(tree)
            nodes.append(current_tree)
            current_tree = tree
        else:
            try:
                n = int(i)
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

            current_tree.set_root_val(n)
            current_tree = nodes.pop()

        print('End', i, current_tree, nodes, '\n\n')
    return current_tree


def build_parse_tree_binary(math_exp: str) -> BinaryTree:
    tokens = math_exp.split() if ' ' in math_exp else split_math_exp_wo_spaces(math_exp)
    print('splitted', tokens)
    current_tree: BinaryTree = BinaryTree('')
    nodes = [current_tree]

    for i in tokens:
        print('Start', i, current_tree, nodes)
        if i == '(':
            tree = BinaryTree('')
            current_tree.insert_left(tree)
            nodes.append(current_tree)
            current_tree = tree
        elif i == 'not':
            current_tree.reverse = True
        elif i == ')':
            current_tree = nodes.pop()
        elif i in {'and', 'or'}:
            current_tree.set_root_val(i)
            tree = BinaryTree('')
            current_tree.insert_right(tree)
            nodes.append(current_tree)
            current_tree = tree
        else:
            current_tree.set_root_val(i == 'True')
            current_tree = nodes.pop()

        print('End', i, current_tree, nodes, '\n\n')
    return current_tree


def build_parse_tree_original(math_exp: str) -> BinaryTree:
    tokens_list = math_exp.split()
    print('splitted', tokens_list)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)

    for i in tokens_list:
        if i in ['+', '-', '*', '/']:
            tree = stack.pop()
            tree.set_root_val(i)
            stack.push(tree)

        elif i not in ['+', '-', '*', '/']:
            try:
                current_tree = stack.pop()
                current_tree.set_root_val(int(i))
                stack.push(current_tree)

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree: BinaryTree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, 'and': operator.and_, 'or': operator.or_, 'not': operator.not_}

    if parse_tree.left_child and parse_tree.right_child:
        print('LR:', parse_tree.left_child, parse_tree.right_child)
        fn = operates[parse_tree.key]
        if parse_tree.reverse:
            return operator.not_(fn(evaluate(parse_tree.left_child), evaluate(parse_tree.right_child)))
        return fn(evaluate(parse_tree.left_child), evaluate(parse_tree.right_child))
    else:
        print(f'Returning {parse_tree.key}')
        if parse_tree.reverse:
            return operator.not_(parse_tree.key)
        return parse_tree.key


def print_exp(tree: BinaryTree) -> str:
    
    def _print_exp(tree: BinaryTree) -> str:
        s_val = ""
        if tree:
            s_val = _print_exp(tree.get_left_child())
            s_val = s_val + str(tree.get_root_val())
            s_val = s_val + _print_exp(tree.get_right_child())
        return s_val

    return f'({_print_exp(tree)})'


if __name__ == "__main__":
    pt: BinaryTree = build_parse_tree("( ( ( 2 * 7 ) + 8 ) * 4 )")
    print(pt)
    print(evaluate(pt))
    pt: BinaryTree = build_parse_tree_binary("not ( not True or False )")
    print('FINALLY:', pt)
    print(evaluate(pt))


# BinaryTree(
#                           +,
#      BinaryTree(, BinaryTree(*, BinaryTree(2, None, None), BinaryTree(7, None, None)), None), BinaryTree(8, None, None))
