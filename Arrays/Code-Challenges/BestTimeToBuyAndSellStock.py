"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # buy starts on the first day being the 0th index of the list
        buy = prices[0]
        # profit starts at 0 duh
        profit = 0
        
        # loop through the prices
        for num in prices:
            # if we find a where the number is less than the buy
            if num < buy:
            # the new buy will be equal to the current number
                buy = num
            # if the number is greater than the buy
            if num > buy:
                # calculate the max profit compared to the previous profit vs the number we are on minus the buy
                profit = max(profit, num - buy)
        # after the loop return the profit
        return profit
        # Time Complexity: o(n) at worst we need to loop through the whole list
        # Space Complexity: o(1) no external DS

output = Solution()
print(output.maxProfit([7,1,5,3,6,4]))
print(output.maxProfit([73,11,53,35,62,41]))
