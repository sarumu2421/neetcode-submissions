# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        curr = head

        while curr: 
            curr = curr.next 
            length += 1
        
        remove_index = length - n 

        #case where you want to remove the head
        if remove_index == 0:
            return head.next

        count = 1
        curr = head
        
        while curr: 
            if count == remove_index: 
                if curr.next:
                    curr.next = curr.next.next 
                else: 
                    curr.next = None 
                break
            else: 
                curr = curr.next
                count += 1 
        
        return head


