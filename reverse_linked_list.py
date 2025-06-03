# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
 
# 1 -> 2 -> 3 -> 4
# 4 -> 3 -> 2 -> 1
# 1 <- 2 <- 3 <- 4

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    

    
def traverse(head: ListNode):
    current_node = head
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next
        
    
      
node5 = ListNode()
node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head_1= None
head_2 = ListNode(1, None)
head_3 = node1

# test cases
## case-1: None
## case-2: 1
## case-3: 1 -> 2 -> 3 -> 4

print("Case 1:")
s1= Solution()
reverse_1=s1.reverseList(head_1)
traverse(reverse_1)

print("Case 2:")
reverse_2=s1.reverseList(head_2)
traverse(reverse_2)
print("Case 3: ")
reverse_3=s1.reverseList(head_3)
traverse(reverse_3)


