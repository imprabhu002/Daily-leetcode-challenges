from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [sum(row) for row in grid]
        ones_col = [sum(col) for col in zip(*grid)]
        prabhu = [[2 * ones_row[i] + 2 * ones_col[j] - n - m for j in range(n)] for i in range(m)]

        return prabhu
