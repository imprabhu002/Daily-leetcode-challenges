from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        # Initialize the triangle with the first row containing just a 1.
        triangle = [[1]]

        # Generate the remaining rows.
        for i in range(1, numRows):
            # Create a new row with the first element being 1.
            row = [1]

            # Calculate the values in the middle of the row.
            for j in range(1, i):
                # Each value is the sum of the two values directly above it.
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            # Add the last element of the row, which is also 1.
            row.append(1)

            # Append the newly created row to the triangle.
            triangle.append(row)

        return triangle

# Example usage:
numRows = 5
solution = Solution()
result = solution.generate(numRows)
for row in result:
    print(row)
