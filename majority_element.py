class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        countdir = {}
        for element in nums:
            if element not in countdir:
                countdir[element] = 1
            else:
                countdir[element] += 1

            if countdir[element] > (len(nums) / 2):
                return element


list1 = [3, 3, 4]  # should be 3
print(Solution().majorityElement(list1))
