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
        
    def binaryToLinkedList(self,head):
        myList = []
        curr = head
        
        while curr:
            myList.append(curr.data)
            curr = curr.next
        
myList = [1,0,1]
output = ''.join([str(ele) for ele in myList])
print(int(output,2))
