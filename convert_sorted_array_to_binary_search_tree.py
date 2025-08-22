# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # The length of nums is odd
        middle_nums_index = len(nums) // 2
        middle_nums_value = nums[middle_nums_index]
        for i in range(len(nums)):
            
            





        # the length of nums is even