class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return [numsU:=sorted(set(nums)), min(len(nums) - (bisect_left(numsU, numsU[i] + len(nums)) - i) for i in range(len(numsU)))][1]
