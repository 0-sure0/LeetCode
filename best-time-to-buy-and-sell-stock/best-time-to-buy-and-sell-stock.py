class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profits = [0]
        for i in range(1, len(prices)):
            if min < prices[i]:
                profits.append(prices[i] - min)
            else:
                min = prices[i]
        
        return max(profits)