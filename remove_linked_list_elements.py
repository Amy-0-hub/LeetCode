# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional




# 1 -> 2 -> 6 -> 3
# remove: 1 ->2 ->3
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev_node =ListNode(0)  #dummy node
        prev_node.next = head
        current_node =prev_node
        while current_node.next is not None:
            if current_node.next.val == val:
                current_node.next= current_node.next.next    
            else:
                current_node = current_node.next

        return prev_node.next


node4 = ListNode(3, None) 
node3 = ListNode(6, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head=node1

s1=Solution()
print(s1.removeElements(head, 6))
            
        

        


            

        
            
