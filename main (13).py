class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None            #starting point of LinkedList
        
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:        #if the list is empty
            self.head = new_node    
        else:
            temp = self.head
            while temp.next:
                temp = temp.next       
            temp.next = new_node
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")
        
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
        
    def count(self):
        count=0
        temp=head
        while temp:
            count=count+1
            temp=temp.next
        return(count)
    
    def insert_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
            
    def delete_beginning(self):
        self.head=self.head.next
        
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=none
        
ll=LinkedList()     
ll.insert_end(10)
ll.insert_beginning(900000)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_end(50)
ll.delete_beginning()
ll.display()
print("sum of the elements in linked list is ")
ans=ll.add_ll()
print(ans)
