from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # count = 0
        # pointer1 = 0
        # pointer2 = 0
        # g.sort()
        # s.sort()
        # while pointer1 < len(g) and pointer2 < len(s):
        #     if s[pointer2] >= g[pointer1]:
        #         count += 1
        #         pointer1 += 1
        #         pointer2 += 1
        #     else:
        #         pointer2 += 1
                    
        # return count
        g.sort()
        s.sort()
        i = j = 0

        while i < len(s) and j < len(g):
            if g[j] <= s[i]:
                j += 1
            i += 1
        return j
    

# case test
# g = [1,2,3]
# s = [1,1]
# g = [1,2]
# s = [1,2,3]
g = [10, 9, 8, 7]
s = [5, 6, 7, 8]

object = Solution()
print(object.findContentChildren(g, s))



