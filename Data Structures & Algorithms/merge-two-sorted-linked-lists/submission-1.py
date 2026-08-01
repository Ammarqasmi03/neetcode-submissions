# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # curr1 = list1
        # curr2 = list2
        # dummy = ListNode(-1)
        # tail = dummy


        # while curr1 != None and curr2 != None:
        #     if curr1.val <= curr2.val:
        #         tail.next = curr1
        #         curr1 = curr1.next

        #     else:
        #         tail.next = curr2
        #         curr2 = curr2.next
            
        #     tail = tail.next
            

        # if curr1 != None:
        #     while curr1 != None:
        #         tail.next = curr1
        #         tail = tail.next
        #         curr1 = curr1.next

        # else:
        #     while curr2 != None:
        #         tail.next = curr2
        #         tail = tail.next
        #         curr2 = curr2.next

        # return dummy.next


        curr = head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return head.next

            

      
                
        