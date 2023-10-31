from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [0] * n  # Initialize arr with all zeros
        xor_result = 0  # Initialize the XOR result
        
        for i in range(n):
            if i == 0:
                arr[i] = pref[i]
                xor_result = pref[i]
            else:
                # Use the XOR property to calculate arr[i]
                arr[i] = pref[i] ^ xor_result
                xor_result ^= arr[i]
        
        return arr

# Example usage:
solution = Solution()
pref = [3, 0, 9, 6]
arr = solution.findArray(pref)
print(arr)
