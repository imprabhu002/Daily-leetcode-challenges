# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Base cases
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        if n % 2 == 0:
            return []  # No possible full binary tree with even number of nodes

        # List to store the possible full binary trees
        result = []

        # Iterate through all possible left subtree node counts (from 1 to n-1)
        # and divide the remaining nodes for the right subtree
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes

            # Generate all possible left and right subtrees recursively
            left_subtrees = self.allPossibleFBT(left_nodes)
            right_subtrees = self.allPossibleFBT(right_nodes)

            # Connect the left and right subtrees to the root node (with value 0)
            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(0)
                    root.left = left_subtree
                    root.right = right_subtree
                    result.append(root)

        return result

# Example usage:
n = 7
solution = Solution()
trees = solution.allPossibleFBT(n)
for tree in trees:
    # Process or display the trees as needed
    pass
