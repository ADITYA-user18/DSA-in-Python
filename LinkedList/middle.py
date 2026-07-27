class Node:
    def __init__(self,val):
        self.val = val
        self.next = None




n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)


Nodes = [n1,n2,n3,n4,n5,n6,n7,n8]


for i in range(len(Nodes)-1):
    Nodes[i].next = Nodes[i+1]


head = n1

curr = head


slow = curr
fast = curr

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print(slow.val)
