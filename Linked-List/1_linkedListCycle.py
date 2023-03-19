class Node:
    def __init__(self,dataval = None,next = None):
        self.data = dataval
        self.next = next
        
        
        
class LinkedList:
    def __init__(self,head=None):
        self.head = None
        
    def addElement(self,data):
        node = Node(data,self.head)
        self.head = node
        print("Data inserted")
        
    def displayElements(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
        
    # check if Cycle Exists
    def hasCycles(self,head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
            if fast == slow:
                return True
        return False




llist = LinkedList()
llist.addElement(20)
llist.addElement(40)
llist.displayElements()