class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(ord('A') + remainder) + result
            columnNumber //= 26
        return result

# Test cases
solution = Solution()
print(solution.convertToTitle(1))  # Output: "A"
print(solution.convertToTitle(28))  # Output: "AB"
print(solution.convertToTitle(701))  # Output: "ZY"
