"""
Main a set for:
1. row
2. col
3. square: (row / 3) * 3 + (col / 3)

Data Structure: {int: set()}
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        row_cache = {i: set() for i in range(9)} 
        col_cache = {i: set() for i in range(9)}
        square_cache = {i: set() for i in range(9)}

        for row in range(9):
            for col in range(9):
                curr_digit = board[row][col]
                if curr_digit == ".":
                    continue
                square_index = (row // 3) * 3 + (col // 3)
                if (curr_digit in row_cache[row] or
                    curr_digit in col_cache[col] or
                    curr_digit in square_cache[square_index]):
                    return False
                
                row_cache[row].add(curr_digit)
                col_cache[col].add(curr_digit)
                square_cache[square_index].add(curr_digit)
        
        return True
