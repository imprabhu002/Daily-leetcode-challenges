class Solution:
    def minSpeedOnTime(self, dist, hour):
        def can_reach_office(dist, speed, hour):
            total_time = 0
            n = len(dist)
            for i in range(n - 1):
                total_time += (dist[i] + speed - 1) // speed
            total_time += dist[n - 1] / speed
            return total_time <= hour

        left, right = 1, 10**7
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if can_reach_office(dist, mid, hour):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
