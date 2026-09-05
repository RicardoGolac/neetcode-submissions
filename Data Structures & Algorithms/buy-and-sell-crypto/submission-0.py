class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Go sequentially through array.
        # Keep track of current min and maxProfit
        # Only change min if its less than current min.
        # Only update maxProfit if new profit is bigger.
        min = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            price = prices[i]
            if price > min:
                diff = price - min
                if diff > maxProfit:
                    maxProfit = diff
            if price < min:
                min = price
            
        return maxProfit