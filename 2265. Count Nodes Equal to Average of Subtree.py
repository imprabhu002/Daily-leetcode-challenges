class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Helper function to calculate the sum and count of nodes in the subtree
        def calculate_average(node):
            if not node:
                return (0, 0)
            
            left_sum, left_count = calculate_average(node.left)
            right_sum, right_count = calculate_average(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            return (total_sum, total_count)
        
        # Helper function to check if a node's value is equal to the subtree's average
        def is_value_equal_to_average(node):
            if not node:
                return True
            
            left_sum, left_count = calculate_average(node.left)
            right_sum, right_count = calculate_average(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            subtree_average = total_sum // total_count
            
            return node.val == subtree_average
        
        # Start the recursion from the root
        def count_nodes_with_average_value(node):
            if not node:
                return 0
            
            count = is_value_equal_to_average(node)
            
            left_count = count_nodes_with_average_value(node.left)
            right_count = count_nodes_with_average_value(node.right)
            
            return count + left_count + right_count
        
        return count_nodes_with_average_value(root)

# Example usage:
# Construct the binary tree and call the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
result = solution.averageOfSubtree(root)
print(result)  # Output: 4
