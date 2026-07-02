class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        length = len(prices)

        if (length == 1):
            return profit

        for i in range(1, length, 1):
            if prices[i] < buy:
                buy = prices[i]
            
            else:
                if profit < prices[i] - buy:
                    profit = prices[i] - buy

        return profit       
