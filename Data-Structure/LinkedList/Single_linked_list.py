class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
    def at_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def at_any_pos(self,pos,data):
        new_node=Node(data)
        current=self.head
        for i in range(pos-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node 
    def reverse(self):
        prev=None
        current=self.head
        while current:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
        self.head=prev

ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.display()
ll.at_any_pos(2,3)
ll.display()
ll.reverse()
ll.display()
        