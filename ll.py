class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def insert_at_beginning(self,data):
        new=Node(data)        
        new.next=self.head
        self.head=new
    def insert_at_end(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def insert_at_i(self,data,p):
        new=Node(data)
        temp=self.head
        for _ in range(0,p-1):
            temp=temp.next        
        new.next=temp.next
        temp.next=new
    def delete_from_beginning(self):
        if not self.head:
            return
        self.head=self.head.next
    def delete_from_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delete_by_value(self,v):
        temp=self.head
        if temp.data==v:
            self.head=temp.next
            return
        while temp:
            if temp.next.data == v:
                temp.next=temp.next.next
                return
            temp=temp.next
            
            
        
        
l=ll()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
l.insert_at_beginning(1)
l.insert_at_end(40)
l.insert_at_i(2,2)
l.delete_from_beginning()
l.delete_from_end()
l.delete_by_value(20)

l.traverse()