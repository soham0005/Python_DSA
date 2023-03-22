class Node:
    def __init__(self,dataval = None, next = None):
        self.data = dataval
        self.next = next
        
    

class Linkedlist:
    def __init__(self):
        self.head = None
        
        
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        print("Data Inserted at the Start")
        
    def displayElements(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
        
    def reverseLinkedList(self):
        if(self.head is None or self.head.next is None):
            return self.head
        
        prev = None
        curr = self.head
        
        while(curr is not None):
            forward =  curr.next
            curr.next = prev
            prev = curr
            curr = forward
        return prev
                   
    
    
    
'''


None 

'''   
        
        
mylist = Linkedlist()
mylist.insert_at_beginning(10)
mylist.insert_at_beginning(20)
mylist.insert_at_beginning(30)
mylist.insert_at_beginning(40)
mylist.displayElements()
