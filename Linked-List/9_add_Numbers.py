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
        tempArray1 = []
        tempArray2 = []
        temp = l1
        while temp:
            tempArray1.append(temp.val)
            temp = temp.next
        tempArray1 = tempArray1[::-1]
        temp = l2
        while temp:
            tempArray2.append(temp.val)
            temp = temp.next
        tempArray2 = tempArray2[::-1]
        
            