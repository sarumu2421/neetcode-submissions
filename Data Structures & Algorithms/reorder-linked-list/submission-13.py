# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #fast and slow pointer approach to find middle node and split list
        fast = head 
        slow = head 
        prev = None

        #loop tail pointer to get to end: 
        while fast and fast.next: 
            fast = fast.next.next 
            prev = slow
            slow = slow.next 
        
        #now slow will be exactly at the middle point 
        if prev:
            prev.next = None # split the list
        list2 = slow 
        list1 = head

        
        #reverse list2 
        prevNode = None

        while list2 != None: 
            nextNode = list2.next 
            list2.next = prevNode 

            #move the pointers down
            prevNode = list2
            list2 = nextNode

        #reset list2 to head of reversed list
        list2 = prevNode 

        # merge both lists in place (no dummy node)
        while list1 and list2: 
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
        
        if list2:
            tail.next = list2

    
            


        
        