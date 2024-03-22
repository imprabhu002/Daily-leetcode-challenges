class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        tmp=head
        while tmp:
            arr.append(tmp.val)
            tmp=tmp.next
        return arr == arr[::-1]
