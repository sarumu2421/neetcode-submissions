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


        #merge list1 with new list2 
        dummy = ListNode() 
        tail = dummy 

        index = 1
        while list1 and list2: 
            if index % 2 == 1:
                tail.next = list1 
                list1 = list1.next  
            else: 
                tail.next = list2 
                list2 = list2.next  
            tail = tail.next
            index += 1
        
        if list1: 
            tail.next = list1
        elif list2: 
            tail.next = list2
            
        return dummy.next
    
            


        
        