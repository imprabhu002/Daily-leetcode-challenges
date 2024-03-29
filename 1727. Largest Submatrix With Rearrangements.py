class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for c in range(len(matrix[0])):
            h = 0
            for r in range(len(matrix)):
                h = h+1 if matrix[r][c] == 1 else 0
                matrix[r][c] = h
        result = 0
        for row in matrix:
            row.sort()
            for c in range(len(row)):
                result = max(result, (len(row)-c) * row[c])
        return result
