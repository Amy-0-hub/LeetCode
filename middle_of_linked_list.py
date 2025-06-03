# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# 1 -> 2 -> 3 -> 4 -> 5
## return 3 -> 4 -> 5


# 1 -> 2 -> 3 -> 4 -> 5 -> 6
## return 4 -> 5 -> 6
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next

        if count == 1:
            return head

        middle_check = count // 2

        if middle_check == 0:  # return the second one
            middle_node_number = count / 2 + 1

        else:  # return the middle one
            middle_node_number = count / 2
        # while middle_node_number >1:
        #     head = head.next
        #     middle_node_number -= 1

        for i in range(int(middle_node_number)):
            head = head.next

        return head


def traverse(head: ListNode):
    cur_node = head
    while cur_node is not None:
        print(cur_node.val)
        cur_node = cur_node.next


# node6 = ListNode(6, None)
node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head1 = node1

s = Solution()
r1 = s.middleNode(head1)
traverse(r1)

print("case 2; ")
head2 = ListNode(1, None)
r2 = s.middleNode(head2)
traverse(r2)
