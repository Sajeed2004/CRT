class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None            #starting point of LinkedList
        
    def insert(self,data):
        new_node=Node(data)
        if(self.head.next==None):
            self.head=new_node    #links new node to head node
        else:
            temp=self.head
            while temp.next==None:
            temp=temp.next        #moves temp node for
            temp.next=new_node
            
    def display(self):
        temp=self.node
        while temp:
            print(temp.data)
            temp=temp.next
  
            
ll=LinkedList()     
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.display()