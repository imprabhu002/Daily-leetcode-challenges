class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool: 
        def leaf_lst(root) : return [] if not root else [root.val] if not root.left and not root.right else leaf_lst(root.left) + leaf_lst(root.right) 
        
        return leaf_lst(root1) == leaf_lst(root2)
