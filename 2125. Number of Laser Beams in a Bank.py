class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        output = 0
        for b in bank:
            l = b.count('1')
            if l != 0:
                lasers.append(l)
        i = 0
        while i < len(lasers)-1:
            output+=lasers[i]*lasers[i+1]
            i+=1

        return output  
