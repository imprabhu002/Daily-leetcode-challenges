class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =  len(nums)
        start, end =[1] * n, [1] * n

        for i in range(1, n):start[i] = start[i-1] * nums[i-1]
        for i in range(n-2, -1 ,-1): end[i] = end[i+1] * nums[i+1]
        return [start[i] * end[i] for i in range(n)]
