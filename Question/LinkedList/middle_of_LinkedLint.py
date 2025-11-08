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

    # this is slow and fast method in which slow pointer move with 1 and fast move with 2 till fast go to last node of ll    
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    

ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.display()
print(ll.middle())



