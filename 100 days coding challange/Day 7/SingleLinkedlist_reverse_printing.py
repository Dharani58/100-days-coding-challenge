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

    def display(self):
        if self.root is None:
            print('SLL is empty')
            return
        temp=self.root
        while temp is not None:
            print(temp.val,"->",end='')
            temp=temp.next
        print()

    def display_reverse_iterative(self):
        if self.root is None:
            print("SLL is empty")
            return
        stack = []
        temp = self.root
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        while stack:
            print(stack.pop(), "->", end='')
        print()

    def display_reverse(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            print("SLL is empty")
            return
        if node.next is not None:
            self.display_reverse(node.next)
        print(node.val, "->", end='')

s=SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)
s.addNewNode(45)
s.display()
s.display_reverse_iterative()
s.display_reverse()