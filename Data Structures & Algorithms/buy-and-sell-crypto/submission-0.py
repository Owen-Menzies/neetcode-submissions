class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices)):
            for j in prices[i:]:
                max_prof = max(max_prof,j-prices[i])
        return max_prof