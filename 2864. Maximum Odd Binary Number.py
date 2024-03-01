class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return ((c := Counter(s))["1"] - 1) * "1" + c["0"] * "0" + "1"
