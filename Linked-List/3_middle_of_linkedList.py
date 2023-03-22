# Bruteforce approach is to traverse list and get the length and then return length/2

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
            
    def lengthOfList(self):
        count = 0
        curr = self.head
        while(curr is not None):
            count +=1
            curr = curr.next
        print(f'Length of Linked List is {(count // 2)}')
        
        
        temp = self.head
        ans = 0
        while(ans < count):
            temp = temp.next
            ans +=1
        print(temp)
        
            
        
mylist = Linkedlist()
mylist.insert_at_beginning(10)
mylist.insert_at_beginning(20)
mylist.insert_at_beginning(30)
mylist.insert_at_beginning(40)
mylist.insert_at_beginning(40)

mylist.displayElements()
mylist.lengthOfList()