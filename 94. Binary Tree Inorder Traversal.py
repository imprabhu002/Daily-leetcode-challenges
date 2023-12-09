class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderTraversalRecursive(root, result)
        return result
    
    def inorderTraversalRecursive(self, node, result):
        if node:
            self.inorderTraversalRecursive(node.left, result)
            
            result.append(node.val)
            self.inorderTraversalRecursive(node.right, result)
