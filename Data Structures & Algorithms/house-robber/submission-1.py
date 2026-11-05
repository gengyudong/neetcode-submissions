class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_2, rob_1 = 0, 0
        
        for num in nums:
            amount_rob = rob_2 + num
            new = max(rob_1, amount_rob)
            rob_2 = rob_1
            rob_1 = new
        
        return rob_1



"""
At house i:

1) Not rob -> rob(i-1)
2) Rob     -> rob(i-2) + nums[i]

max(not rob, rob)
"""