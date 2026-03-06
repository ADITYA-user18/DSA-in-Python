class Solution(object):
  def maxProfit(self, prices):
    buy = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
            buy = min(buy,prices[i])
            profit = prices[i] - buy
            max_profit = max(profit,max_profit)
    return max_profit
