from .binary_tree import BinaryTree
from .models import Node


def run():
    node_40 = Node(40)
    node_35 = Node(35)
    node_32 = Node(32)
    node_55_0 = Node(55)
    node_55_1 = Node(55)
    node_50 = Node(50)
    node_53_0 = Node(53)
    node_53_1 = Node(53)
    node_52 = Node(52)

    auto_node_40 = Node(40)
    auto_node_35 = Node(35)
    auto_node_32 = Node(32)
    auto_node_55_0 = Node(55)
    auto_node_55_1 = Node(55)
    auto_node_50 = Node(50)
    auto_node_53_0 = Node(53)
    auto_node_53_1 = Node(53)
    auto_node_52 = Node(52)

    node_40.set_left(node_35)
    node_40.set_right(node_55_0)

    node_35.set_left(node_32)

    node_55_0.set_left(node_50)
    node_55_0.set_right(node_55_1)

    node_50.set_right(node_53_0)

    node_53_0.set_right(node_53_1)

    node_53_1.set_left(node_52)

    manual_binary_tree = BinaryTree(node_40)
    auto_binary_tree = BinaryTree(auto_node_40)
    auto_binary_tree.insert(auto_node_35)
    auto_binary_tree.insert(auto_node_55_0)
    auto_binary_tree.insert(auto_node_32)
    auto_binary_tree.insert(auto_node_50)
    auto_binary_tree.insert(auto_node_55_1)
    auto_binary_tree.insert(auto_node_53_0)
    auto_binary_tree.insert(auto_node_53_1)
    auto_binary_tree.insert(auto_node_52)

    manual_binary_tree.direct_order()
    auto_binary_tree.direct_order()
    print('________')
    manual_binary_tree.indirect_order()
    auto_binary_tree.indirect_order()
    print('________')
    manual_binary_tree.symmetric_order()
    auto_binary_tree.symmetric_order()
    print('________')

    for i in range(len(manual_binary_tree)):
        print(
            manual_binary_tree._direct_order[i], '<>', auto_binary_tree._direct_order[i], ' | ',
            manual_binary_tree._indirect_order[i], '<>', auto_binary_tree._indirect_order[i], ' | ',
            manual_binary_tree._symmetric_order[i], '<>', auto_binary_tree._symmetric_order[i], ' |'
        )
