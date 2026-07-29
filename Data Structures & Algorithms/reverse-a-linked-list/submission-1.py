class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head

        # while curr != None:
        #     nxt = curr.next
        #     curr.next = prev

        #     prev = curr
        #     curr = nxt

        # head = prev 
        
        # return head

        prev = None
        curr = head
        while curr:
            # reverve the address
            nxt = curr.next
            curr.next = prev
            # moves both pointer forward
            prev = curr
            curr = nxt

        return prev