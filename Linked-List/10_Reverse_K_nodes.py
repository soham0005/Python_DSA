# Approach:- First Reverse k nodes then apply recursion for the rest
# For recursion check if forward is not None then Recursively Call Function
# Return prev

def lengthOfList(head):
    temp = head
    count = 0
    
    while temp:
        count += 1
        temp = temp.next
        
    return count

def reverseGroupOfK(head,k,length):
    if length < k:
        return head
    else:
        count = 0
        prev,forward = None,None
        curr = head
        
        while curr != None and count < k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            count += 1
        
        if forward != None:
            head.next = reverseGroupOfK(forward,k,length-k)
            
        return prev
    

# Main Function
def reverseKNodesOfList(head,k):
    length = lengthOfList(head)
    return reverseGroupOfK(head,k,length)