class Solution(object):
    def minPatches(self, nums, n):
        patches=0
        count=1
        i=0
        while count<=n:
            if i<len(nums) and nums[i]<=count:
                count+=nums[i]
                i+=1
            else:
                patches+=1
                count+=count
        return patches
