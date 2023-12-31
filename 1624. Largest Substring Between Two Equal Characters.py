class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max([s.rfind(char) - s.find(char) - 1 for char in set(s)], default=-1)
