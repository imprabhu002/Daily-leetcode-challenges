class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev pointer to the node just before the sublist to be reversed
        for _ in range(left - 1):
            prev = prev.next
        
        # Initialize pointers for reversing the sublist
        curr = prev.next
        next_node = None
        
        # Reverse the sublist between left and right
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp
        
        # Connect the reversed sublist back to the main list
        prev.next.next = curr
        prev.next = next_node
        
        # If left is 1, update the head pointer
        if left == 1:
            head = prev.next
        
        return head
