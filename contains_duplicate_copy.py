class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] == nums[j]) and (abs(i - j) <= k):
        #             return True
        # return False

        # method 2: sliding window
        window = set()
        L = 0 # Left Pointer
        for R in range(len(nums)):  #right pointer via for loop
            if R - L > k:
                window.remove(nums[L])
                L +1 = 1
            if nums[R] in window:
                return True
            window.add(nums[R])
            
        return False






nums1 = [1, 2, 3, 1,2,3]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums1, k))

# for i in range(0,4):
#     for j in range(i+1, 4):
#         print('i=', i)
#         print('j=', j)
