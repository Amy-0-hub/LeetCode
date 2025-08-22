from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        
        # if len(nums1) > len(nums2):
        #     for n in nums2:
        #         if n in nums1 and len(res) < len(nums2):
        #             res.append(n)
        #             nums1.remove(n)
        # elif len(nums2) > len(nums1):
        #     for n in nums1:
        #         if n in nums2 and len(res) < len(nums1):
        #             res.append(n)
        #             nums2.remove(n)
        # else:
        #     for n in nums1:
        #         if n in nums2:
        #             res.append(n)
        #             nums2.remove(n)
        # return res

        # method: hash map
        map = {}

        for num in nums1:
            map[num] = map.get(num, 0) + 1
        
        res = []

        for num in nums2:
            if num in map and map[num] > 0:
                res.append(num)
                map[num] -= 1
        return res

# case test
# nums1 = [1,2,2,1]
# nums2 = [2]
# nums1 = [4,9,5]
nums1 = [9,4,9,8,4]
nums2 = [4,9,5]
# nums1 = [1,2]
# nums2 = [1,1]
# nums1 = [3,1,2]
# nums2 = [1,1]
s = Solution()
print(s.intersect(nums1, nums2))