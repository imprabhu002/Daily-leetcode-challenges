class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0

        for c in range(ord('a'), ord('z') + 1):
            char = chr(c)
            left, right = float('inf'), float('-inf')


            for i in range(len(s)):
                if s[i] == char:
                    left = min(left, i)
                    right = max(right, i)


            if left < right:
                result += len(set(s[left + 1:right]))

        return result

solution = Solution()
s = "bbcbaba"
print(solution.countPalindromicSubsequence(s))
