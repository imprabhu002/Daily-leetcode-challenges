class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        q = head
        for i in range(n):
            q = q.next
        if not q:
            return p.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head
