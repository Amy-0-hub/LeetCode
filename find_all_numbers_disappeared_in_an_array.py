from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        res = []
        for num in range(1, len(nums)+1):
            if num not in nums1:
                res.append(num)
        return res

# case test
nums = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDisappearedNumbers(nums))