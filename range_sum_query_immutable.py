from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # self.nums = nums
        self.prefix =[] #method prefix sums
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)       

    def sumRange(self, left: int, right: int) -> int:
        # result = 0
        # for index in range(left, right+1):
        #     result += self.nums[index]
        # return result
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0  else 0
        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
left = 0
right = 2
obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
print(param_1)