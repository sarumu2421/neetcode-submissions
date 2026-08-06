# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #don't return anything, modify in place
        #fast and slow pointer approach to find middle node and split list
        fast = head.next 
        slow = head 

        #loop tail pointer to get to end: 
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
        
        #now slow will be at the middle point 
        list2 = slow.next 
        slow.next = None # split the list so list1 ends here
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
            #temp variables
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            #now shift pointers to next nodes
            list1 = next1
            list2 = next2
  

    
            


        
        