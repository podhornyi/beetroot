#                     insert        update       delete
# Linked list (2)      O(1)           O(1)        O(1)
#

from dataclasses import dataclass


@dataclass
class Node:
    payload: dict = None
    prev_node: 'Node' = None
    next_node: 'Node' = None


node_1 = Node()
node_2 = Node()
node_3 = Node()
node_x = Node()

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_1

node_1.prev_node = node_3
node_2.prev_node = node_1
node_3.prev_node = node_2

node_x.next_node = node_3
node_x.prev_node_node = node_2
node_2.next_node = node_x
node_3.prev_node = node_x

