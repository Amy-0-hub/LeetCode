class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
     
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2




class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

        if ptr1 is not None:
            previous_node.next = ptr1

        if ptr2 is not None:
            previous_node.next = ptr2
            
        return head.next



def traverse(head: ListNode):
    cur_node = head
    while cur_node is not None:
        print(cur_node.val)
        cur_node = cur_node.next

# case:
# list1 = [1, 3, 4]
# list2 = [1, 2, 4]
node13 = ListNode(4, None)
node12 = ListNode(3, node13)
node11 = ListNode(1, node12)
head1 = node11

node23 = ListNode(4, None)
node22 = ListNode(2, node23)
node21 = ListNode(1, node22)
head2 = node21

e1= Solution2()
r1 = e1.mergeTwoLists(head1, head2)
traverse(r1)


        

        