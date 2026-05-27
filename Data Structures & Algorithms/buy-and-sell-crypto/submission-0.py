class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {}
        max_profit = 0
        sell = 0

        for buy in range(len(prices)):
            profit[buy] = profit.get(buy, 0)

            while sell < len(prices):
                current_profit = prices[sell] - prices[buy]
                max_profit = max(current_profit, max_profit)
                sell += 1

            profit[buy] = max_profit
            sell = buy+1

        return max_profit
        