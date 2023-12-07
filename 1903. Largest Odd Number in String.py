class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num[:max((r for r, d in enumerate(num) if int(d) % 2 != 0), default=-1) + 1]
