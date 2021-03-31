class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min = prices[0]
        diff = 0
        
        for i in range(len(prices)):
            temp = prices[i] - min
            if temp > diff:
                diff = temp
            if prices[i] < min:
                min = prices[i]
                       
        return diff
            
        
