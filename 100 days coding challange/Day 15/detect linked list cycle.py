class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

node_a = Node(1)
node_b = Node(2)
node_a.next = node_b

solver = Solution()
print(f"Does the first list have a cycle? {solver.hasCycle(node1)}")
print(f"Does the second list have a cycle? {solver.hasCycle(node_a)}")