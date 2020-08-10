class Node:
    def __init__(self,info=None,next=None,prev=None):
        self.info=info
        self.next=next
        self.prev=prev
    def __str__(self):
        return str(self.info)
''''''''''''''''''''''''''''''''''''

def azNode():      #circular, bi-dir, linked list of a-z
    head=Node('a')
    
    savehead=head
    prevSave=head
    for i in range(1,27):
        head.next=Node(chr(ord('a')+i))
        if(i!=1):
            head.prev=prevSave 
        prevSave=head
        head=head.next
        
    ''''''''''''''''''''''''
    #now connect the chain as circular
    ''''''''''''''''''''''''
    head.next=savehead #z-->a
    savehead.prev=head #z<---a
    return savehead


def caesarEncode(st,k):
    st2=''
    for i in st:
        head=azNode()
        while(i != head.info and head is not None):
            head=head.next
        #now we found the char, lets caesar it k times
        for i in range(k):
            head=head.next
        st2+=head.info
    
    return st2

         
def caesarDecode(st,k):
    st2=''
    for i in st:
        head=azNode()
        while(i != head.info and head is not None):
            head=head.next
        #now we found the char, lets de-caesar it MINUS k times
        for i in range(k):
            head=head.prev
        st2+=head.info
    
    return st2

def main():
    st='wxyza'
    print(caesarEncode(st, 100))
    
main()

        
    