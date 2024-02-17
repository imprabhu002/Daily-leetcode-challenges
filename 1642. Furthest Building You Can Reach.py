from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heappop(heap)
                if bricks < 0:
                    return i
        return len(heights) - 1
