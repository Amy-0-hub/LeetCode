class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # function signature
        new_list = []
        for i in range(len(nums)):
            if nums[i] not in new_list:
                new_list.append(nums[i])

        if new_list == nums:
            return False
        else:
            return True


import copy

l1 = [1, 2]
l2 = copy.copy([1, 2])

print(l1 == l2)
