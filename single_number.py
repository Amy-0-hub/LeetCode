from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        same_value_list = []
        nums.sort()
        for i in range(1,len(nums)):
                if nums[i] == nums[i-1]:
                    same_value_list.append(nums[i])

        for element in nums:
            if element not in same_value_list:
                return element
            
                

# case test
# nums = [2,2,1]
nums = [4,1,2,1,2]
# nums = [1]
# nums = [1,0,1]
print(Solution().singleNumber(nums))            