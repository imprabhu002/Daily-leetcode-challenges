class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Create an array to keep track of parent nodes for each node.
        parents = [-1] * n

        for i in range(n):
            left, right = leftChild[i], rightChild[i]

            # Check for multiple parents.
            if left != -1:
                if parents[left] != -1:
                    return False
                parents[left] = i
            if right != -1:
                if parents[right] != -1:
                    return False
                parents[right] = i

        # Count the number of nodes without parents.
        root_count = parents.count(-1)

        # There should be exactly one node without a parent (the root).
        if root_count != 1:
            return False

        # Check for cycles.
        visited = [False] * n

        def hasCycle(node):
            if visited[node]:
                return True
            visited[node] = True

            left, right = leftChild[node], rightChild[node]

            if left != -1 and hasCycle(left):
                return True
            if right != -1 and hasCycle(right):
                return True

            return False

        # Check for cycles starting from the root.
        root = parents.index(-1)
        if hasCycle(root):
            return False

        # Check if all nodes are reachable.
        return visited.count(True) == n

