class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_price = prices[0]
        for i in range(1, len(prices)):
            if prev_price > prices[i]:
                prev_price = prices[i]
            else:
                profit += prices[i] - prev_price
                prev_price = prices[i]
        
        return profit
                