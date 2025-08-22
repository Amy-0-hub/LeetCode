from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # ptr1 = 0  # for nums1
        # ptr2 = 0  # for nums2

        # while ptr1 < len(nums1) and ptr2 < len(nums2):
        #     if nums1[ptr1] == nums2[ptr2] and ptr2 < len(nums2)-1:
        #         for num in nums2[ptr2+1:]:
        #             if num > nums2[ptr2]:
        #                 res.append(num)
        #                 break
        #         else:
        #             res.append(-1)
                    
        #         ptr1 += 1
        #         ptr2 = 0
        #     elif nums1[ptr1] == nums2[ptr2] and ptr2 == len(nums2)-1:
        #         res.append(-1)
        #         ptr1 += 1
        #         ptr2 = 0
        #     else:
        #         ptr2 += 1
        
        # return res

        # method2 : brute force solution
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

        

                
                    
                

                
        


# case test
# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
# nums1 = [2,4]
# nums2 = [1,2,3,4]
# nums1 = [4,1,2]
# nums2 = [1,2,3,4]
# nums1 = [2,1,3]
# nums2 = [2,3,1]
nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))
