from typing import List
# You must write an algorithm with o(log n) runtime complexity. (don't loop through the list; use a binary search)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = int((left + right) / 2)
            # print(mid)

            if nums[mid] == target:
                # print(mid)
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

        return left


# case test
nums = [1,3,5,6]
target = 2
s = Solution()
print(s.searchInsert(nums, target))
