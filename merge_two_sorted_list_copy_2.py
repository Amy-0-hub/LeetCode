# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = ListNode(0, None)
        previous_node = head
        ptr1, ptr2 = list1, list2
        while (ptr1 and ptr2) is not None:
            if ptr1.val <= ptr2.val:
                previous_node.next = ptr1
                previous_node = ptr1
                ptr1 = ptr1.next    
            else:
                previous_node.next = ptr2
                previous_node = ptr2
                ptr2 = ptr2.next
        if ptr1 is None:
            previous_node.next = ptr2
        if ptr2 is None:
            previous_node.next = ptr1
        return head.next
        
        
def traverse(head: ListNode):
    cur_node = head
    while cur_node is not None:
        print(cur_node.val)
        cur_node = cur_node.next

# case 1:
node32 = ListNode(4, None)
node22 = ListNode(2, node32)
node12 = ListNode(1, node22)
list1 = node12

node31 = ListNode(4, None)
node21 = ListNode(3, node31)
node11 = ListNode(1, node21)
list2 = node11

e1 = Solution()
r1 = e1.mergeTwoLists(list1, list2)
traverse(r1)