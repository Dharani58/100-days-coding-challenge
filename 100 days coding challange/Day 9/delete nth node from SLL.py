class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.root = None

    def addNewNode(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def removeNthFromEnd(self, n):
        dummy = Node(0)
        dummy.next = self.root

        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            if fast is None:
                print(f"Error: The list has fewer than {n} nodes.")
                return
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        self.root = dummy.next

    def display(self):
        if self.root is None:
            print('SLL is empty')
            return
        temp = self.root
        while temp is not None:
            print(temp.val, "->", end='')
            temp = temp.next
        print()

s=SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)
s.addNewNode(45)
s.display()
s.removeNthFromEnd(2)
s.display()