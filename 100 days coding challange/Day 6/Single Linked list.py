class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.root=None

    def addNewNode(self,val):
        n=Node(val)
        if self.root is None:
            self.root=n
            return
        temp=self.root
        while temp.next is not None:
            temp=temp.next
        temp.next=n

    def insert_at_position(self,val,pos):
        n=Node(val)
        if pos==1:
            n.next=self.root
            self.root=n
            return
        temp=self.root
        len=1
        while temp!=None and len<pos-1:
            temp=temp.next
            len+=1
        print(f"inserted at position {pos} successfully")
        if temp==None:
            return
        n.next=temp.next
        temp.next=n

    def delete_at_index(self, index):
        if self.root is None:
            print("Linked list is empty.")
            return
        if index < 0:
            print("Index cannot be negative.")
            return
        if index == 0:
            self.root = self.root.next
            print(f"Node at index 0 has been deleted.")
            return
        temp = self.root
        current_index = 0
        while temp is not None and current_index < index - 1:
            temp = temp.next
            current_index += 1
        if temp is None or temp.next is None:
            print(f"Index {index} is out of bounds.")
            return
        temp.next = temp.next.next
        print(f"Node at index {index} has been deleted.")

    def display(self):
        if self.root is None:
            print('SLL is empty')
            return
        temp=self.root
        while temp is not None:
            print(temp.val,"->",end='')
            temp=temp.next
        print()

s=SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)
s.addNewNode(45)
s.display()
s.insert_at_position(90,3)
s.display()
s.delete_at_index(2)
s.display()