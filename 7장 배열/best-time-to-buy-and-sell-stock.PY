# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Maxbenefit = 0

        # for i,val in enumerate(prices):
        #     if i == len(prices)-1:
        #         break            
        #     list = prices[i+1:]
        #     if Maxbenefit < max(list)-val:
        #         Maxbenefit = max(list)-val
            
        # return Maxbenefit
#타임아웃
        min = sys.maxsize
        max = -sys.maxsize
        for price in prices:
            if min > price:
                min = price
            if max < price-min:
                max = price-min

        return max

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))           