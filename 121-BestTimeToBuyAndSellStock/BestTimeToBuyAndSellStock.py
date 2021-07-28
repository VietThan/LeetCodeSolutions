# Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        
        minPrice = 10000
        max = 0
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if (prices[i]-minPrice) > max:
                max = prices[i]-minPrice
                
        return max
        
