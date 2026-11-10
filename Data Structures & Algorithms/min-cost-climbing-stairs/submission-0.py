"""
dp[i] = min cost of reaching this step, i = 0-indexed

dp[0] = 0
dp[1] = 0
dp[2] = min(dp[0] + cost[0], dp[1] + cost[1])
dp[3] = min(dp[1] + cost[1], dp[2] + cost[2])
...
dp[n+1]
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range (2, n + 1):
            dp[i] = min(
                dp[i - 2] + cost[i - 2],
                dp[i - 1] + cost[i - 1]
            )
        
        return dp[n]
        
        