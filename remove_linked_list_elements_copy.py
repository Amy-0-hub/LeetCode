class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next

from typing import Optional  
class Solution:
    def removeElements(self, head: Optional[ListNode], val:int) ->Optional[ListNode]:
        prev_node = ListNode()
        prev_node.next = head
        cur_node = prev_node
        while cur_node.next is not None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

        return prev_node.next
