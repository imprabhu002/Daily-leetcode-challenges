class Solution:
    def numberOfWays(self, corridor: str) -> int:
        modulo = 10**9 + 7
        n = len(corridor)
        m = corridor.count('S')

        if m == 0 or m % 2:
            return 0

        output, idx1, idx2 = 1, 0, 0

        while idx1 < n:
            idx1 = idx2
            counter = 0

            while idx1 < n and counter < 2:
                counter += corridor[idx1] == 'S'
                idx1 += 1

            counter, idx2 = 0, idx1

            while idx2 < n and corridor[idx2] == 'P':
                counter += 1
                idx2 += 1

            if idx2 == n:
                break

            output *= (counter + 1)

        return output % modulo
