from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if 0 in nums:
        #         nums.remove(0)
        #         nums.append(0)

        # method 2: two pointers technique
        l = 0 # left pointer
        for r in range(len(nums)):   # right pointer
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
          
            
            
                
# case test
# nums = [1, 0, 0, 1]
nums = [0,1,0,3,12]
s = Solution()
s.moveZeroes(nums)
