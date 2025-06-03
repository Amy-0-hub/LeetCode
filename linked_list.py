class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next


# 1 -> 2 -> 3
node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

head = node1


# 指针变量：存储object地址的变量
# how to traverse a linked list, and print every value
def traverse(head: Node):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


array1 = list(range(100))
# yaqin todo: create a linked list from above array


def from_array(array: list) -> Node:
    next_node = None  # a dummy node
    for e in reversed(array):
        current_node = Node(e, next_node)
        next_node = current_node

    return current_node


def linked_list(array: list):
    prev_node = Node(array[-1], None)
    for element in reversed(array[:-1]):
        cur_node = Node(element, prev_node)
        prev_node = cur_node

    return cur_node


# example_node = from_array(array1)
# traverse(example_node)


# yaqin todo: how to find if a value is in the linked list, define function by yourself
value_1 = 2
value_2 = 5


def check(data: int, head: Node):

    current_node = head
    while current_node is not None:
        value1 = current_node.value
        if value1 == data:
            print(f"This value of {data} is in the linked list.")
            return True
        current_node = current_node.next

    print(f"This value of {data} is not in the linked list.")
    return False


s1 = linked_list(array1)
check(value_1, s1)


# while True:
#     current_node = current_node.next
#     if current_node.value == data:
#         print(f"This value of {data} is in the linked list")
#     else:
#         print(f"The value of {data} is invalid.")


# how to insert a node into the linked list
# 1 -> 2 -> 3  ==>  1 -> 2 -> 5 -> 3

print("traverse before insert")
traverse(head)

node_new = Node(5)
current_node = head
while True:
    if current_node.value == 2:
        node_new.next = current_node.next
        current_node.next = node_new
        break
    else:
        current_node = current_node.next

print("traverse after insert")
traverse(head)
