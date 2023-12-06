class Solution:
    def totalMoney(self, n: int) -> int:
        week1=[1,2,3,4,5,6,7]
        ans=0
        for i in range(n):
            ans+=week1[i%7]
            week1[i%7]+=1
        return ans
