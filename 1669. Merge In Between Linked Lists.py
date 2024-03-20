class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head=list1
        i,j=0,0
        while list1:
            if i==a-1:  
                pos1=list1
            if j==b:   
                pos2=list1
            i,j=i+1,j+1
            list1=list1.next


        s=list2 
        e=list2  
        while e.next: 
            e=e.next 
        pos1.next=s
        e.next=pos2.next

        return head
