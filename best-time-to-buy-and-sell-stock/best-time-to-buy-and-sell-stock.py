class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit = 0
        mn_price = sys.maxsize
        ln = len(prices)
        
        for price in prices:
            mn_price = min(mn_price, price)
            mx_profit = max(mx_profit, price-mn_price)
        
        return mx_profit     
        
        
        
​
