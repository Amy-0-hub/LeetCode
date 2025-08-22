from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     if nums[0] == 1:
        #         return 1
        #     else:
        #         return 0
        # if 1 not in nums:
        #     return 0

        # count = 1 
        # cur_count = []
        # for i in range(1,len(nums)):
        #     if nums[i-1] == nums[i] and nums[i-1] == 1:
        #         count += 1
        #         cur_count.append(count)
        #     else:
        #         count = 1
        # if len(cur_count) >= 1:
        #     cur_count.sort()
        #     return cur_count[-1]
        # return count
        res = 0
        count = 0
        
        for n in nums:
            if n == 0:
                count = 0
            else: count += 1
        
            if res < count:
                res = count
        return res

# case test
# nums1 = [1]
# nums1 = [1,1,0,1,1,1]
# nums1 = [1,1,1,0,1,1]
nums1 = [1,0,1,1,0,1]
# nums1 = [0,0]
# nums1 = [1,1]
# nums1 = [1,0]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums1))
            
    

