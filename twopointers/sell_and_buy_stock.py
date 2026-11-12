class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #must buy after you sell
        #if next day is less then make that the new buy
        
        l,r = 0, 1
        max_profit = 0

        while r < len(prices):
            buy = prices[l] 
            sell = prices[r]

            if buy < sell:
                max_profit = max(max_profit, sell - buy)
            else:
                l = r

            r += 1

        return max_profit