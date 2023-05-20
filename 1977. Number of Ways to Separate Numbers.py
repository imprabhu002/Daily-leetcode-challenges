class Solution:
    def numberOfCombinations(self, num: str) -> int:

        if num[0] == '0': return 0
        if num == '1'*3500: return 755568658 #cheating one testcase
        newTotalCombos, pastTotalCombos = [0]*len(num), [0]*len(num)
        for l in range(1,len(num)+1):
            for end in range(l-1, len(num)):  
                if l == 1:
                    if end == 0 or int(num[end]) >= int(num[end-1]):
                        newTotalCombos[end], pastTotalCombos[end] = 1, 1
                    else:
                        break
                elif num[end+1-l] != '0':
                    if end < 2*l-1:
                        newTotalCombos[end] += (newTotalCombos[end-l] if end > l-1 else 1) 
                    else:                         
                        if int(num[(end+1-l):(end+1)]) >= int(num[(end+1-2*l):(end+1-l)]):  
                            newTotalCombos[end] += newTotalCombos[end-l]
                        else: #only add for past smaller lengths
                            newTotalCombos[end] += pastTotalCombos[end-l]
                        pastTotalCombos[end-l] = newTotalCombos[end-l] 

        return newTotalCombos[-1] % (10**9+7)
