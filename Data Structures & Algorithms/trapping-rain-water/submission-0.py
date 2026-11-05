class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        height_left_cache = {i:0 for i in range(len(height))}
        height_right_cache = {i:0 for i in range(len(height))}
        output = 0

        curr_max = 0
        # To find max height on the left
        for i in range(len(height)):
            height_left_cache[i] = curr_max
            curr_max = max(curr_max, height[i])

        curr_max = 0
        # To find max height on the right
        for i in range(len(height) - 1, -1, -1):
            height_right_cache[i] = curr_max
            curr_max = max(curr_max, height[i])

        for i in range(len(height)):
            water = min(height_left_cache[i], height_right_cache[i]) - height[i]
            if water > 0:
                output += water

        return output
