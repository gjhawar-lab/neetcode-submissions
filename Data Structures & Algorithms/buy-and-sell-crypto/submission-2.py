class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # buy day (left pointer)
        max_profit = 0
        
        for r in range(len(prices)):  # sell day (right pointer)
            if prices[r] < prices[l]:
                # Found a lower buy price — move window start
                l = r
            else:
                # Calculate profit and update max
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
        
        return max_profit
        