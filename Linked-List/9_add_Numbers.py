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
 
 
    def addNumbers(self,l1,l2):
        dummy = Node()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1  = l1.val if l1 else 0
            val2  = l2.val if l2 else 0
            result = val1 + val2 + carry
            carry = result // 10
            result = result % 10
            curr.next  = Node(result)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next