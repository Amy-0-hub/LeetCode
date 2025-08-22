from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = []
        # for i in range(1,len(prices)):
        #     for j in range(len(prices)):
        #         diff_price = prices[i] - prices[j]
        #         # print(diff_price)
        #         if diff_price > 0 and i > j:
        #             profit.append(diff_price)
                
        # if len(profit) > 0:
        #     profit.sort(reverse=True)
        #     print(profit)
        #     return profit[0]
        # else:
        #     return 0
        
        # method 2: two pointer
        l , r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r += 1
        return maxP
                    
        
# case test
# prices1 = [7, 6, 4]
prices2 = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices2))