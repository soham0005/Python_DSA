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
    
    def palindromeList(self):
        
        
        #Brute Force Approach
        
        # if self.head is None or self.head.next is None:
        #     return True
        # temp = self.head
        # prev = None
        # curr = self.head
        
        # #Reversal of the Linked List
        # while(curr is not None):
        #     forward = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = forward
            
        # #Now check if list is palindrome or not
        # while(temp is not None and prev is not None):
        #     if(temp.data == prev.data):
        #         temp = temp.next
        #         prev = prev.next
        #     else:
        #         return False
        # return True
        
        #Using List:-
        myArray = []
        curr = self.head
        while(curr is not None):
            myArray.append(curr.data)
            curr = curr.next
        print("Checking if it is Palindrome")
        print(myArray == myArray[::-1])
        
        
        
        
                
                
myList = LinkedList()
myList.insert_at_beginning(1)
myList.insert_at_beginning(1)
myList.insert_at_beginning(2)
myList.insert_at_beginning(1)

myList.printElements()
myList.palindromeList()
