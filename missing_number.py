from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        
        # method 2
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
            
# case test
nums1 = [3, 0, 1]
s = Solution()
print(s.missingNumber(nums1))

