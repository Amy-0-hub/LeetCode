from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total = 0
        for i in range(len(timeSeries)-1):
            total += min(timeSeries[i+1] - timeSeries[i], duration)

        return total + duration









        # res = []
        # if duration == 0:
        #     return 0
        
        # for t in timeSeries:
        #     for num in range(t, t+duration):
        #         res.append(num)
        # res = list(set(res))    

        # return len(res)

            
        

            
# case test
# timeSeries = [1,4]
# duration = 2
# timeSeries = [1, 2]
timeSeries = [1,2,3,4,5,6,7,8,9]
duration = 10000
obj = Solution()
print(obj.findPoisonedDuration(timeSeries, duration))


