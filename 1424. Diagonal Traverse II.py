class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = {}
        for row in range(len(nums)-1,-1,-1):
            for col in range(len(nums[row])-1,-1,-1):
                if row+col in dic.keys():
                    dic[row+col].append(nums[row][col])
                else:
                    dic[row+col] = [nums[row][col]]

        ans = []
        dic = sorted(dic.items(), key=lambda x: x[0])
        for key,val in dic:
            ans += val
        return ans
