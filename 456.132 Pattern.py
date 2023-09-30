class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n < 3:
            return False

        # Create a stack to store potential '2' values
        stack = []
        # Initialize the maximum value to be negative infinity
        max_val = float('-inf')

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            num = nums[i]

            # Check if the current number is greater than the maximum value
            if num < max_val:
                return True  # Found a valid 132 pattern

            # Remove elements from the stack that are less than the current number
            while stack and num > stack[-1]:
                max_val = stack.pop()

            # Add the current number to the stack
            stack.append(num)

        return False  # No valid 132 pattern found

# Example usage:
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.find132pattern(nums)) 
