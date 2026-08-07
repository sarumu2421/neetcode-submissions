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

        #loop tail pointer to get to end: 
        while fast != None: 
            fast = fast.next.next 
            slow = slow.next 
        
        #now slow will be exactly at the middle point 

        list2 = slow 
        list1 = head

        #reverse list2 
        prev = None

        while list2 != None: 
            nextNode = list2.next 
            list2.next = prev 

            #move the pointers down
            prev = list2
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
            index += 1

        tail = tail.next 
        return dummy.next
    
            


        
        