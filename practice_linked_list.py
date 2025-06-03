class Node:
    def __init__(self, value: int, next = None):
        self.value = value
        self.next = next

array1 = list(range(100))
# yaqin todo: create a linked list from above array
def linked_list(array:list, head:Node):
    head = array[0]
    current = head
    for i in range(len(array)):
        current = current.next
    return current

linked_list(array1)