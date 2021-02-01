from typing import Optional, Any
import operator


class Tree:

    def __init__(self,
                 root: Any,
                 left: Optional['Tree'] = None,
                 right: Optional['Tree'] = None):
        self.root = root
        self.left: Optional['Tree'] = left
        self.right: Optional['Tree'] = right
        self.need_to_reverse_result = False

    def insert_left(self, tree: 'Tree'):
        self.left = tree

    def insert_right(self, tree: 'Tree'):
        self.right = tree

    def __str__(self):
        return f'Tree({self.root}; {self.left}; {self.right})'


def parse_math_expr(expression: str) -> Optional[Tree]:
    tokens = expression.split()
    print(tokens)
    current_tree: Tree = Tree('')
    stack = [current_tree]
    for token in tokens:
        print('Start', token, current_tree)
        if token == '(':
            tree = Tree('')
            current_tree.insert_left(tree)
            stack.append(current_tree)
            current_tree = tree
        elif token == ')':
            current_tree = stack.pop()
        elif token in {'-', '+', '*', '/'}:
            current_tree.root = token
            tree = Tree('')
            current_tree.insert_right(tree)
            stack.append(current_tree)
            current_tree = tree
        else:
            try:
                n = float(token)
            except ValueError:
                raise Exception(f'Not a valid integer: {token}')

            current_tree.root = n
            current_tree = stack.pop()
        print('End', token, current_tree, '\n\n')

    return current_tree


def parse_bool_expr(expression: str) -> Optional[Tree]:
    tokens = expression.split()
    print(tokens)
    current_tree: Tree = Tree('')
    stack = [current_tree]
    for token in tokens:
        print('Start', token, current_tree)
        if token == '(':
            tree = Tree('')
            current_tree.insert_left(tree)
            stack.append(current_tree)
            current_tree = tree
        elif token == 'not':
            current_tree.need_to_reverse_result = True
        elif token == ')':
            current_tree = stack.pop()
        elif token in {'and', 'or'}:
            current_tree.root = token
            tree = Tree('')
            current_tree.insert_right(tree)
            stack.append(current_tree)
            current_tree = tree
        else:
            current_tree.root = token == 'True'
            current_tree = stack.pop()
        print('End', token, current_tree, '\n\n')

    return current_tree

def evaluate(tree: Tree):
    operators = {
        '*': operator.mul,
        '-': operator.sub,
        '+': operator.add,
        '/': operator.truediv,
        'and': operator.and_,
        'or': operator.or_
    }

    if tree.left and tree.right:
        result = operators[tree.root](evaluate(tree.left), evaluate(tree.right))
        if tree.need_to_reverse_result:
            return not result
        return result
    else:
        if tree.need_to_reverse_result:
            return not tree.root
        return tree.root


math_expression = '( ( ( 1 - 2 ) * 3 ) - ( ( 21 / 4 ) + 44 ) )'
bool_expression = 'not ( ( True or False ) and not False )'

if __name__ == '__main__':
    tree = parse_math_expr(math_expression)
    print(evaluate(tree), tree)
    tree = parse_bool_expr(bool_expression)
    print(f'Result: {evaluate(tree)}, {tree}')



    #                       Tree(*; ; )

               # Tree(-; ; )                                  Tree(3; None; None)

# Tree(1; None; None)    Tree(2; None; None)


# Tree(or; Tree(True; None; None); Tree(False; None; None))