from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
        return res
    
# case test
# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 =[4,9,5]
nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersection(nums1, nums2))