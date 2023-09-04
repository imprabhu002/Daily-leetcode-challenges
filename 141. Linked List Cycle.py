class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False  # If there are less than 2 nodes, there can't be a cycle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Move the slow pointer one step
            fast = fast.next.next  # Move the fast pointer two steps

            if slow == fast:
                return True  # If they meet, there is a cycle

        return False 
