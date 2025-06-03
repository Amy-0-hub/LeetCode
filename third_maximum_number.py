nums1 = [8, 9, 10, 2, 3, 4, 5, 1, 10]


class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        list1 = []
        for k in range(len(nums)):
            if nums[k] not in list1:
                list1.append(nums[k])

        N = len(list1)

        for i in range(0, 3):
            for j in range(0, N - 1):
                if list1[j] > list1[j + 1]:
                    new = list1[j]
                    list1[j] = list1[j + 1]
                    list1[j + 1] = new
            print(list1)

        if len(list1) < 3:
            return list1[-1]
        else:
            return list1[-3]


s = Solution()
print(s.thirdMax(nums1))
# nums1=set(nums)
# nums1=list(nums1)
# nums1.sort()
# if nums1 is not None and len(nums1) < 3:
#     return nums1[-1]
# if nums1 is not None and len(nums1) >=3:
#     return nums1[-3]
