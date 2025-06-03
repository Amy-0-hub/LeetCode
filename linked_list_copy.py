class Node:
    def __init__(self, value:int, next=None):
        self.value = value
        self.next = next

# 1 -> 2 -> 3, None
node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

head = node1


# traverse
def traverse(head:Node):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

# traverse(head)



# create a linked list from an array
array1=list(range(100))

def from_array(array:list):
    next_node = None   #dummy node
    for element in reversed(array):
        current_node = Node(element, next_node)
        next_node = current_node
    return current_node

    
e1 =from_array(array1)
traverse(e1)





# check if a value is in the linked list, define a function
def check(value:int, head:Node):
    current_node = head
    while current_node is not None:
        if current_node.value == value:
            print(f"This value of {value} is in the linked list.")
            return True
        current_node = current_node.next

    print(f"This value of {value} is not in the linked list.")
    return False

    
val=2
check(val, e1)

vall=100
check(vall, e1)



#insert a value in a linked list
## before insert: 1 -> 2 -> 3
## after:         1 -> 2 -> 5 -> 3



node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

head = node1


current_node = head
new_node = Node(5)
while current_node is not None:
    if current_node.value == 2:
        new_node.next = current_node.next
        current_node.next = new_node
        break
    else:
        current_node = current_node.next
        
traverse(head)       


    
