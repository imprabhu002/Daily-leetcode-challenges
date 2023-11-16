from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set(nums)

        for i in range(2**n):
            binary_str = bin(i)[2:].zfill(n)  # Convert to binary and zero-fill
            if binary_str not in seen:
                return binary_str

        # This should not happen according to the problem constraints
        return ""
