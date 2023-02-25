class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l = prices[0]
        m = 0
        n = len(prices)
        
        for i in range(1,n):
            m = max(m, prices[i]-l)
            l = min(l, prices[i])
            
        return m   