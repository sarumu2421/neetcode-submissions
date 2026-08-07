# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if there is a cycle, it will just loop forever 

        #2 pointers 

        pointer1 = head 
        pointer2 = head 

        #iterate through the list 
        while pointer2 is not None and pointer1 is not None: 
            pointer2 = pointer2.next
            pointer1 = pointer1.next.next  
        
            if pointer1 == pointer2: #means both pointers met, so there is a cycle 
                return True 
        
        return False 

        

        