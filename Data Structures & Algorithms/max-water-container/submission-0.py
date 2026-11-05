class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_p = 0
        right_p = len(heights) - 1
        max_area = 0

        while left_p < right_p:
            width = right_p - left_p
            height = min(heights[left_p], heights[right_p])
            max_area = max(max_area, width * height)

            if heights[left_p] < heights[right_p]:
                left_p += 1
            else:
                right_p -= 1
        
        return max_area

        