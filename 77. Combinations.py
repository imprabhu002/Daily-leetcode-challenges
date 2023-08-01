from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(1, [])
        return result

# Example 1
sol = Solution()
n = 4
k = 2
combinations = sol.combine(n, k)
print(combinations)

# Example 2
n = 1
k = 1
combinations = sol.combine(n, k)
print(combinations)
