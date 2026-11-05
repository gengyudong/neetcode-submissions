class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remainder, path):
            # Check for success condition
            if remainder == 0:
                result.append(path.copy())
                return

            # Check for failure condition
            if remainder < 0:
                return
            
            # Backtracking logic
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remainder - nums[i], path)
                path.pop()

        backtrack(0, target, [])
        
        return result
        