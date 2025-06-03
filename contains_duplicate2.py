class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]) and (abs(i-j) <=k):
                    return True
        return False
            
                

                    
        
nums1=[1,2,3,1,2,3]
k=2
s = Solution()
s.containsNearbyDuplicate(nums1,k)

# for i in range(0,4):
#     for j in range(i+1, 4):
#         print('i=', i)
#         print('j=', j)
       
    
