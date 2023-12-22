class Solution:
    def maxScore(self, s: str) -> int:
        zeros_left, ones_right = 0, s.count('1')
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1

            current_score = zeros_left + ones_right
            max_score = max(max_score, current_score)

        return max_score

# Example usage
solution = Solution()
s = "011101"
result = solution.maxScore(s)
print(result)
