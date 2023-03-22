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
    
    def deleteDuplicates(self):
        if self.head is None:
            return None
        curr = self.head
        while curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return self.head

            