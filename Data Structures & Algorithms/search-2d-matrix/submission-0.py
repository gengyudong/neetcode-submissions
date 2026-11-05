class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(lst: List[int], target: int) -> bool:
            left = 0
            right = len(lst) - 1

            while left <= right:
                mid = (left + right) // 2

                if lst[mid] == target:
                    return True
                
                elif lst[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            return False
        
        left_r = 0
        right_r = len(matrix) - 1

        while left_r <= right_r:
            mid = (left_r + right_r) // 2
            
            if target < matrix[mid][0]:
                right_r = mid - 1
            
            elif target > matrix[mid][-1]:
                left_r = mid + 1
            
            else:
                return binary_search(matrix[mid], target)

        return False   