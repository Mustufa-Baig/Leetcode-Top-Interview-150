class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buy = prices[0]
        N = len(prices)
        for i in range(0,N):
            sell=prices[i]
            if buy < sell: 
                total += sell - buy
            buy = sell
        return total

