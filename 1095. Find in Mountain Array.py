class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_peak(mountain_arr):
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = left + (right - left) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search_asc(left, right, target, mountain_arr):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def binary_search_desc(left, right, target, mountain_arr):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        peak_index = find_peak(mountain_arr)
        target_index = binary_search_asc(0, peak_index, target, mountain_arr)
        
        if target_index == -1:
            target_index = binary_search_desc(peak_index, mountain_arr.length() - 1, target, mountain_arr)
        
        return target_index

# Example usage:
# mountain_arr = MountainArray([1, 2, 3, 4, 5, 3, 1])
# target = 3
# solution = Solution()
# result = solution.findInMountainArray(target, mountain_arr)
# print(result)  # This will print the index of the target element.
