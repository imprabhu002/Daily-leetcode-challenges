class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            // If target is found
            if (nums[mid] == target) {
                return mid;
            }

            // If target is smaller, move the end
            if (target < nums[mid]) {
                end = mid - 1;
            } 
            // If target is larger, move the start
            else {
                start = mid + 1;
            }
        }
        // If target is not found, start will be the insertion position
        return start;
    }
}
