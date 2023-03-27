class Node:
    def __init__(self,dataval=None,next=None):
         self.data = dataval
         self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        print("Data Inserted at the Start")
    
    def intersection(self,headA,headB):
        if headA is not None or headB is not None:
            return None
        
        tempA = headA
        tempB = headB
        
        while tempA != tempB:
            tempA = tempB if tempA is None else tempA.next
            tempB = tempA if tempB is None else tempB.next
        
        return tempA
    
            
                
    
    
list1 = LinkedList()
list2 = LinkedList()