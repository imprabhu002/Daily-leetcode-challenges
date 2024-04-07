class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0

        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            elif c == ')':
                cmax -= 1
                cmin -= 1
            elif c == '*':
                cmax += 1
                cmin -= 1

            if cmax < 0:
                return False
            cmin = max(cmin, 0)

        return cmin == 0
