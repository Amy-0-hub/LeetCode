class ListNode:
    def __init__(self, value:int, next=None):
        self.value = value
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        if cur_node is None:
            return None
        next_node = cur_node.next
        cur_node.next = None

        while next_node is not None:
            store = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = store
        
        return cur_node
    
def traverse(head:ListNode):
    cur_node = head
    while cur_node is not None:
        print(cur_node.value)
        cur_node = cur_node.next

# test case
## case 1: None
## case 2: 1
## case 3: 1 -> 2 -> 3 -> 4
node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head1= None
head2=ListNode(1, None)
head3 = node1

print("Case 1: ")
e = Solution()
r1 = e.reverseList(head1)
traverse(r1)

print("Case 2: ")
r2=e.reverseList(head2)
traverse(r2)

print("Case 3: ")
r3=e.reverseList(head3)
traverse(r3)