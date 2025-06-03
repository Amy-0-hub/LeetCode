class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # input -> [1, 1, 2]
        # numbs -> [1, 1, 2]
        new_list = []
        k = 0
        for element in nums:
            if element not in new_list:
                new_list.append(element)
                k += 1

        for i in range(len(new_list)):
            nums[i] = new_list[i]

        return k


input = [1, 1, 2]
solution = Solution()

l = solution.removeDuplicates(input)


print(l)
print(input)
