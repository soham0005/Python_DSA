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
    
    
    def length(self):
        if self.head == None:
            print(0)
            return 0
        else:
            count = 0
            temp = self.head
            while temp:
                count +=1
                temp = temp.next
        print(count)
        return 
    
    
    def printElements(self):
        if self.head == None:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
                
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            print("Node Inserted")
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data,None)
            print("Node Inserted")
            return
    
    def delete_start(self):
        if self.head == None:
            print("List is Empty, Cannot Delete Element")
            return
        else:
            self.head = self.head.next
            print("Deleted")
            return   
        
    def delete_end(self):
        if self.head == None:
            print("Empty Linked List, Cannot Delete Element")
            return
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            print("Last Element Deleted")
                     
           
                
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(30)
    # linked_list.printElements()
    linked_list.insert_at_end(40)
    # linked_list.printElements()
    linked_list.length()
    # linked_list.delete_start()
    linked_list.delete_end()
    linked_list.printElements()

    