class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_buy_price=prices[0]
        for i in prices:
            profit=i-min_buy_price
            max_profit=max(profit,max_profit)
            min_buy_price=min(min_buy_price,i)
            
        return max_profit
        
        