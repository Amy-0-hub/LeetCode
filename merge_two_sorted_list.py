# Definition for singly-linked list.
# A single linked list is a list made up of nodes that consists of two parts.
## 1.data: contains the actual data
## 2.link: contains the address of the next node of the list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        pointer1 = head1
        pointer2 = head2
        result = None

        if head1.val <= head2.val:
            result = head1
            head1 = head1.next
        else:
            result = head2
            head2 = head2.next

        while (pointer1 is not None) and (pointer2 is not None):
            if pointer1.val <= pointer2.val:
                store = pointer1.next
                pointer1.next = pointer2
                pointer1 = store
            else:
                store = pointer2.next
                pointer2.next = pointer1
                pointer2 = store
        return result

class Solution1:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class Solution2:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2

        head = ListNode(0, None)
        previous_node = head
        while (ptr1 is not None) and (ptr2 is not None):
            if ptr1.val < ptr2.val:
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


# list1 = [1, 3, 4]
# lsit2 = [1, 2, 4]
# desired output [1, 2，3, 4，4]

node13 = ListNode(4, None)
node12 = ListNode(3, node13)
node11 = ListNode(1, node12)
head2=node11

node23 = ListNode(4, None)
node22 = ListNode(2, node23)
node21 = ListNode(1, node22)
head1 = node21

solution = Solution1()
r1 = solution.mergeTwoLists(head1, head2)
traverse(r1)
